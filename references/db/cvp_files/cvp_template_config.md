# OCR模板配置-cvp_template_config

## OCR模板配置-主表 t_cvp_template_config

- **表名称：** OCR模板配置-主表
- **表名：** t_cvp_template_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstep2helperstatus | 模板参考字段帮助 | bpchar | 1 |  | √ | '1' | 模板参考字段帮助 |
| 3 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 4 | fstep3helperstatus | 模板识别字段帮助 | bpchar | 1 |  | √ | '1' | 模板识别字段帮助 |
| 5 | fuserid | 用户 | varchar | 50 |  | √ | ' ' | 用户 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cvp_template_config |  | fuserid |
| 2 | pk_t_cvp_template_config |  | fid |
