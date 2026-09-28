# 检测配置-aikm_similar_setting

## 检测配置-主表 t_aikm_similar_setting

- **表名称：** 检测配置-主表
- **表名：** t_aikm_similar_setting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdeleteitem | 相似度 | varchar | 50 |  | √ | ' ' | 相似度,枚举: 0.80 :80% 0.70 :70% 0.60 :60% 0.50 :50% |
| 3 | fbasedatafield | 关联知识库 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_similar_setting_fbasedata |  | fbasedatafield |
| 2 | pk_aikm_similar_setting |  | fid |
