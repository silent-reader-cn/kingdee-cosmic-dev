# 搜索历史表-ocdbd_searchhistory

## 搜索历史表-主表 t_ocdbd_searchhistory

- **表名称：** 搜索历史表-主表
- **表名：** t_ocdbd_searchhistory

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fhistory | 历史搜索 | varchar | 255 |  | √ | ' ' | 历史搜索 |
| 3 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fformid | 所属表单 | varchar | 50 |  | √ | ' ' | 所属表单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_searchhistory |  | fformid,fuserid |
| 2 | pk_ocdbd_searchhistory |  | fid |
