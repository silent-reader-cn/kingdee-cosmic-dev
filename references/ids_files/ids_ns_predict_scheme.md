# 新品实时预测-ids_ns_predict_scheme

## 新品实时预测-主表 t_ids_ns_predict_scheme

- **表名称：** 新品实时预测-主表
- **表名：** t_ids_ns_predict_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 4 | ffirstweekdistributionqty | 初始周铺货量 | numeric | 23 | 10 | √ | 0 | 初始周铺货量 |
| 5 | fmaterialid | 新品 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 9 | fprice | 参考单价 | numeric | 23 | 10 | √ | 0 | 参考单价 |
| 10 | fpredictdata_tag | 实时预测详情数据_详情 | text | 0 |  |  | null | 实时预测详情数据_详情 |
| 11 | fpredictdata | 实时预测详情数据 | varchar | 255 |  | √ | ' ' | 实时预测详情数据 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fcaltime | 计算时间 | timestamp | 0 |  |  | null | 计算时间 |
| 14 | fnumber | 方案编码 | varchar | 255 |  | √ | ' ' | 方案编码 |
| 15 | frequestid | 实时预测ID | varchar | 64 |  | √ | ' ' | 实时预测ID |
| 16 | fpredictstatus | 实时预测状态 | varchar | 50 |  | √ | ' ' | 实时预测状态,枚举: success :成功 fail :失败 processing :处理中 |
| 17 | ffirstdistributiondate | 首次铺货日期 | timestamp | 0 |  |  | null | 首次铺货日期 |
| 18 | fpriceposition | 价格分类 | varchar | 50 |  | √ | ' ' | 价格分类,枚举: high :高 middle :中 low :低 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ids_ns_scheme_status |  | fpredictstatus |
| 2 | idx_ids_ns_scheme_name |  | fname |
| 3 | idx_ids_ns_scheme_number |  | fnumber |
| 4 | idx_ids_ns_scheme_query |  | forgid,fcaltime,fpredictstatus |
| 5 | pk_t_ids_ns_predict_scheme |  | fid |
