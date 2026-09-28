# 新品对应表-ids_new_product

## 新品对应表-主表 t_ids_new_product

- **表名称：** 新品对应表-主表
- **表名：** t_ids_new_product

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fnewmaterialid | 新品编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fsimilarmaterialid | 同类品编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 10 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | forigin | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: ai :AI推荐 manual :手工录入 |
| 13 | fstatus | 退出状态 | varchar | 50 |  | √ | ' ' | 退出状态,枚举: normal :正常 exit :已退出 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fimpperiod | 新品导入期（天） | int2 | 16 |  | √ | 0 | 新品导入期（天） |
| 16 | frelation | 对应关系 | varchar | 30 |  | √ | ' ' | 对应关系,枚举: replace :替代 parallel :并行 new :纯新 |
| 17 | fscore | 相似得分 | numeric | 23 | 10 | √ | 0 | 相似得分 |
| 18 | fnewproductcode | 新品标识 | varchar | 255 |  | √ | ' ' | 新品标识 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | faipriority | AI优先推荐 | varchar | 50 |  | √ | ' ' | AI优先推荐 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ids_newproductcode |  | fnewproductcode |
| 2 | pk_t_ids_new_product |  | fid |
