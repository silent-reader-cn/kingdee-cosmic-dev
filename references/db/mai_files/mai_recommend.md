# 推荐问题-mai_recommend

## 推荐问题-主表 t_mai_recommend

- **表名称：** 推荐问题-主表
- **表名：** t_mai_recommend

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frecommend_tag | 推荐问题_详情 | text | 0 |  |  | null | 推荐问题_详情 |
| 3 | fuser | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | frecommend | 推荐问题 | varchar | 255 |  |  | ' ' | 推荐问题 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mai_recommend |  | fid |
| 2 | idx_mai_recommend_fuser |  | fuser |
