# 库存调整日志-pmm_inventory_log

## 库存调整日志-主表 t_mal_inventorylog

- **表名称：** 库存调整日志-主表
- **表名：** t_mal_inventorylog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fchangeqty | 库存变动数量 | numeric | 23 | 10 | √ | 0 | 库存变动数量 |
| 3 | flockedqty | 锁定库存 | numeric | 23 | 10 | √ | 0 | 锁定库存 |
| 4 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | [自建商品池 pmm_prodmanage](../pmm_files/pmm_prodmanage.md) |
| 5 | fcreatetime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 6 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | fentitybillno | 业务单据编码 | varchar | 225 |  | √ | ' ' | 业务单据编码 |
| 8 | foperationname | 操作名称 | varchar | 225 |  | √ | ' ' | 操作名称,枚举: audit :审核 submit :提交 unsubmit :撤销 cancel :取消 |
| 9 | fservicetype | 服务名称 | bpchar | 1 |  | √ | ' ' | 服务名称,枚举: A :预占 B :释放预占 C :扣减 D :释放扣减 E :修改 |
| 10 | fentityname | 业务对象名称 | varchar | 225 |  | √ | ' ' | 业务对象名称,枚举: pmm_instock :库存调整（采购方） ent_instock :库存调整（供应商） mal_order :商城订单 |
| 11 | fcreatorid | 操作用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fcurrentqty | 现有库存 | numeric | 23 | 10 | √ | 0 | 现有库存 |
| 13 | favailableqty | 可用库存 | numeric | 23 | 10 | √ | 0 | 可用库存 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_inventorylog |  | fid |
| 2 | idx_mal_orderentry_fcreatetime |  | fcreatetime |
| 3 | idx_mal_orderentry_fgoodsid |  | fgoodsid |
