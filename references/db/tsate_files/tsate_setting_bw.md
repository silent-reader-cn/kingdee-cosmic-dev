# 报文配置-tsate_setting_bw

## 报文配置-主表 t_tsate_setting_bw

- **表名称：** 报文配置-主表
- **表名：** t_tsate_setting_bw

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fcontent_tag | 报文内容_详情 | text | 0 |  |  | null | 报文内容_详情 |
| 11 | fenable | 是否启用 | varchar | 50 |  | √ | ' ' | 是否启用,枚举: 0 :禁用 1 :启用 |
| 12 | fpath | 路径 | varchar | 50 |  | √ | ' ' | 路径 |
| 13 | fcontent | 报文内容 | varchar | 255 |  | √ | ' ' | 报文内容 |
| 14 | fbillno | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tsate_settbw_num |  | fbillno |
| 2 | pk_tsate_setting_bw |  | fid |
