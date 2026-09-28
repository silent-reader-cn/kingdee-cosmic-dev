# 常用商品-ocdbd_item_commonuse

## 常用商品-主表 t_ocdbd_itemcommonuse

- **表名称：** 常用商品-主表
- **表名：** t_ocdbd_itemcommonuse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fattentiondate | 关注日期 | timestamp | 0 |  |  | null | 关注日期 |
| 3 | forder | 排序号 | int4 | 32 |  | √ | 0 | 排序号 |
| 4 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fitemid | 商品 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_itemcommonuse |  | fitemid,fuserid |
| 2 | pk_ocdbd_itemcommonuse |  | fid |
