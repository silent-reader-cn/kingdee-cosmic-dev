# 单据demo2（演示）-isc_demo_bill_2

## 单据demo2（演示）-主表 t_isc_demo_bill2

- **表名称：** 单据demo2（演示）-主表
- **表名：** t_isc_demo_bill2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fbill | 单据 | int8 | 64 |  | √ | 0 | 单据demo1（演示） isc_demo_bill_1 |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 9 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_isc_bill_demo_2_b |  | fbillno |
| 2 | pk_t_isc_demo_bill2 |  | fid |

---

## 单据体-子表 t_isc_demo_bill2_e

- **表名称：** 单据体-子表
- **表名：** t_isc_demo_bill2_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fflex | 弹性域 | int8 | 64 |  | √ | 0 | null 002 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 5 | fbase | 基础资料 | int8 | 64 |  | √ | 0 | [弹性域配置测试 isc_demo_flex](../iscb_files/isc_demo_flex.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_demo_bill2_e |  | fentryid |
| 2 | index_isc_bill_demo_e2 |  | fid |
