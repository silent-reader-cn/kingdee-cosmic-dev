# 可销量分配结果表-ococic_allotresult

## 可销量分配结果表-主表 t_ococic_allotresult

- **表名称：** 可销量分配结果表-主表
- **表名：** t_ococic_allotresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fresultcode | 查询唯一标识 | varchar | 80 |  | √ | ' ' | 查询唯一标识 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | freservebaseqty | 渠道占用量(基本单位) | numeric | 23 | 10 | √ | 0 | 渠道占用量(基本单位) |
| 5 | fresultqtykey | 可销量唯一标识 | varchar | 80 |  | √ | ' ' | 可销量唯一标识 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 8 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | finvalidendtime | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 10 | fckey | 渠道范围标识 | varchar | 50 |  | √ | ' ' | 渠道范围标识 |
| 11 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 12 | fresultqtyid | 可销量 | int8 | 64 |  | √ | 0 | 可销量 ococic_allotresultqty |
| 13 | fitemid | 商品 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 14 | fallottype | 共享/独享 | bpchar | 1 |  | √ | ' ' | 共享/独享,枚举: A :共享 B :独享 |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | finvalidbegintime | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 18 | fresultkey | 结果唯一标识 | varchar | 80 |  | √ | ' ' | 结果唯一标识 |
| 19 | fchannelid | 渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 20 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 21 | fstockorgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ococic_allotresult |  | fid |
| 2 | idx_ococic_allotresult_key |  | fresultkey |
| 3 | idx_ococic_allotresult_time |  | finvalidbegintime,finvalidendtime |
| 4 | idx_ococic_allotresult_code |  | fresultcode |
| 5 | idx_ococic_allotresult_ctime |  | fcreatetime |
