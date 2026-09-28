# 同步用户-tsate_declare_dynuser

## 同步用户-主表 t_tsate_declare_dynuser

- **表名称：** 同步用户-主表
- **表名：** t_tsate_declare_dynuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdeclarechannel | 申报通道 | int8 | 64 |  | √ | 0 | 申报通道 tsate_channel |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fuser | 用户名 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | foperatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 同步状态 | varchar | 50 |  | √ | ' ' | 同步状态,枚举: 1 :同步中 2 :同步成功 3 :同步失败 |
| 10 | fcreatorid | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fcreater | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fchannel | 申报通道 | varchar | 50 |  | √ | ' ' | 申报通道,枚举: 1 :金蝶账无忧 3 :神州云合 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tsate_declare_dynuser |  | fbillno |
| 2 | pk_tsate_declare_dynuser |  | fid |
