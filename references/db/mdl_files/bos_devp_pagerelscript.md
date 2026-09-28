# 页面与脚本的关联关系表-bos_devp_pagerelscript

## 页面与脚本的关联关系表-主表 t_meta_scriptrelpage

- **表名称：** 页面与脚本的关联关系表-主表
- **表名：** t_meta_scriptrelpage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fpageid | 页面id | varchar | 36 |  | √ | ' ' | 页面id |
| 3 | fscriptid | 脚本id | varchar | 36 |  | √ | ' ' | 脚本id |
| 4 | fenable | 启用 | varchar | 5 |  | √ | '1' | 启用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_scriptrelpage_pkey |  | fid |
| 2 | idx_kdp_scriptrelpage_num |  | fpageid |
