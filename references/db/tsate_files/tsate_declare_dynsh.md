# 同步税号-tsate_declare_dynsh

## 同步税号-主表 t_tsate_declare_dynsh

- **表名称：** 同步税号-主表
- **表名：** t_tsate_declare_dynsh

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdeclarechannel | 申报通道 | int8 | 64 |  | √ | 0 | [申报通道 tsate_channel](../tsate_files/tsate_channel.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | foperatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 6 | fnsrsbh | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | forg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 同步状态 | varchar | 50 |  | √ | ' ' | 同步状态,枚举: 1 :同步中 2 :同步成功 3 :同步失败 |
| 11 | fcreatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fchannel | 申报通道 | varchar | 50 |  | √ | ' ' | 申报通道,枚举: 3 :神州云合 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tsate_declare_dynsh |  | fid |
| 2 | idx_tsate_declare_dynsh |  | fbillno |
