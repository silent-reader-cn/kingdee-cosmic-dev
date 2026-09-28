# 工作台卡片-bos_nocode_card

## 工作台卡片-主表 t_nocode_card

- **表名称：** 工作台卡片-主表
- **表名：** t_nocode_card

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftitle | 卡片名称 | varchar | 50 |  | √ | ' ' | 卡片名称 |
| 3 | fdeleted | 是否已被删除 | bpchar | 1 |  | √ | '0' | 是否已被删除 |
| 4 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | ftype | 卡片类型 | varchar | 50 |  | √ | ' ' | 卡片类型 |
| 6 | fconfig | 配置信息 | text | 0 |  |  | null | 配置信息 |
| 7 | fapp | 应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 8 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 9 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fform | 表单 | varchar | 36 |  | √ | ' ' | 表单元数据 bos_formmeta |
| 11 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fimage | 图片 | varchar | 500 |  | √ | ' ' | 图片 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_nc_card_type |  | ftype |
| 2 | pk_nocode_card |  | fid |
