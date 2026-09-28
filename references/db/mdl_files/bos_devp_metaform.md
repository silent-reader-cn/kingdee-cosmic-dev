# 运行期表单元数据-bos_devp_metaform

## 运行期表单元数据-主表 t_meta_form

- **表名称：** 运行期表单元数据-主表
- **表名：** t_meta_form

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | id | varchar | 36 |  | √ | ' ' | id |
| 2 | ftype | 类型 | int8 | 64 |  | √ | 1 | 类型 |
| 3 | fkey | 页面标识 | varchar | 36 |  | √ | ' ' | 页面标识 |
| 4 | fnumber | 编码 | varchar | 36 |  | √ | ' ' | 编码 |
| 5 | ftimestamp | ftimestamp | int8 | 64 |  | √ | 0 |  |
| 6 | fdata | 页面运行期元数据 | text | 0 |  |  | null | 页面运行期元数据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fnumber | fnumber,fkey,ftype |
| 2 | fkey | fnumber,fkey,ftype |
| 3 | ftype | fnumber,fkey,ftype |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_form_pkey |  | fnumber,fkey,ftype |
| 2 | idx_meta_form_fid |  | fid |
