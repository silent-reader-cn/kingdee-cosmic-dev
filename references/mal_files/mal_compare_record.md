# 商城对比记录-mal_compare_record

## 商城对比记录-主表 t_mal_comparerecord

- **表名称：** 商城对比记录-主表
- **表名：** t_mal_comparerecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fexpire | 有效时长（分钟） | int4 | 32 |  | √ | 0 | 有效时长（分钟） |
| 4 | foptime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fgoodsid | 商品 | int8 | 64 |  | √ | 0 | 商品管理 pmm_prodmanage |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fopuserid | 操作用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_comparerecord |  | fid |
| 2 | idx_mal_record_foptime |  | foptime |
| 3 | idx_mal_record_fopuserid |  | fopuserid |
| 4 | idx_mal_record_fgoodsid |  | fgoodsid |
