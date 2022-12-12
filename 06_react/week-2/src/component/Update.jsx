import React, { useState } from "react";

export default function Update() {
    const [number, setNumber] = useState(0);

    return (
        <div>
            {/* 버튼을 누르면 1씩 플러스 된다. */}
            <div>{number}</div>
            <button
                // // 일반적 업데이트 방식 : batch 처리되어 총 1번만 실행
                // onClick={() => {
                //     setNumber(number + 1)
                //     setNumber(number + 1)
                //     setNumber(number + 1)
                //     setNumber(number + 1)
                // }}

                // 함수형 업데이트 방식 : 각 1회씩 모여 총 4회 실행
                onClick={() => {
                    setNumber((previousState) => previousState + 1);
                    setNumber((previousState) => previousState + 1);
                    setNumber((previousState) => previousState + 1);
                    setNumber((previousState) => previousState + 1);
                }}
            >
                +
            </button>
        </div>
    );
}
