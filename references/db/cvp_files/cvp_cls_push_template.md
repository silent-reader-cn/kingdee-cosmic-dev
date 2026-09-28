# 组合识别器已发布模版-cvp_cls_push_template

## 组合识别器已发布模版-主表 t_cvp_cls_push_config

- **表名称：** 组合识别器已发布模版-主表
- **表名：** t_cvp_cls_push_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fincludedtemplate | 模版名称 | int8 | 64 |  | √ | 0 | 模板基础资料 cvp_template_base |
| 3 | fkeyoword | 分类关键字 | varchar | 1000 |  |  | ' ' | 分类关键字 |
| 4 | fclassifyid | 组合识别器ID | int8 | 64 |  | √ | 0 | 组合识别器ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cvp_cls_push_config |  | fclassifyid |
| 2 | pk_t_cvp_cls_push_config |  | fid |
