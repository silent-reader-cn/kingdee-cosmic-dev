# 委托盘点记录-fa_inventory_entrust

## 委托盘点记录-主表 t_fa_inventory_entrust

- **表名称：** 委托盘点记录-主表
- **表名：** t_fa_inventory_entrust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finventschemeentryid | 盘点方案 | int8 | 64 |  | √ | 0 | [盘点方案 fa_inventscheme_new](../fa_files/fa_inventscheme_new.md) |
| 3 | finventorytaskid | 盘点任务 | int8 | 64 |  | √ | 0 | [我的盘点任务 fa_inventory_task](../fa_files/fa_inventory_task.md) |
| 4 | fconsignorid | 委托人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | finventoryrecordid | 盘点记录 | int8 | 64 |  | √ | 0 | [盘点记录基础资料 fa_inventory_record_base](../fa_files/fa_inventory_record_base.md) |
| 6 | fconsigneeid | 被委托人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | frealcardid | 实物卡片 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_inventory_entrust |  | fid |
| 2 | idx_fa_inventory_entrust |  | finventoryrecordid |
