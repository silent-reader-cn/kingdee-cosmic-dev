# 资源变更记录-pca_res_history

## 资源变更记录-主表 t_pca_res_history

- **表名称：** 资源变更记录-主表
- **表名：** t_pca_res_history

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foperate | 操作类别 | varchar | 50 |  | √ | ' ' | 操作类别 |
| 3 | fresid | 资源ID | int8 | 64 |  | √ | 0 | 资源ID |
| 4 | foperatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | frestype | 资源类别 | varchar | 100 |  | √ | ' ' | 资源类别,枚举: pca_autoallocscheme :自动分摊方案设置 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | frescontent_tag | 资源内容_详情 | text | 0 |  |  | ' ' | 资源内容_详情 |
| 8 | fresname | 资源名称 | varchar | 255 |  | √ | ' ' | 资源名称 |
| 9 | fresnumber | 资源编码 | varchar | 255 |  | √ | ' ' | 资源编码 |
| 10 | fcreatedtime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 11 | frescontent | 资源内容 | varchar | 255 |  | √ | ' ' | 资源内容 |
| 12 | fversion | 版本号 | int4 | 32 |  | √ | 0 | 版本号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_res_history |  | fresid |
| 2 | pk_pca_res_history |  | fid |
