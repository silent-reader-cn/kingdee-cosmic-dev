# 浮动模板-tctb_template_float

## 浮动模板-主表 t_tctb_template_float

- **表名称：** 浮动模板-主表
- **表名：** t_tctb_template_float

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fcreatedatefield | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 5 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 8 | ftype | 模板类型 | varchar | 36 |  | √ | ' ' | 模板类型 tctb_template_type |
| 9 | fcontent_tag | 模板内容_详情 | text | 0 |  |  | null | 模板内容_详情 |
| 10 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 11 | fbasetemplateid | 基础模板主键id | int8 | 64 |  | √ | 0 | 基础模板主键id |
| 12 | fcontent | 模板内容 | varchar | 255 |  | √ | ' ' | 模板内容 |
| 13 | fhtml_tag | 模板html内容_详情 | text | 0 |  |  | null | 模板html内容_详情 |
| 14 | fhtml | 模板html内容 | varchar | 255 |  | √ | ' ' | 模板html内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_template_float |  | forgid,ftype |
| 2 | pk_tctb_template_float |  | fid |
