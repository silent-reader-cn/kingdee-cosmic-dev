# ai附件模板引用关系-idi_fgptastemplatrefrence

## ai附件模板引用关系-主表 t_idi_fgptastemplatref

- **表名称：** ai附件模板引用关系-主表
- **表名：** t_idi_fgptastemplatref

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 3 | fschemaid | 智能数据洞察方案id | int8 | 64 |  | √ | 0 | 智能数据洞察方案id |
| 4 | fhandletype | 记录类型 | varchar | 30 |  | √ | 'fgptas_attachtemplate' | 记录类型,枚举: fgptas_attachtemplate :ai财务助手附件模板 fgptas_rule_repo :规则库 |
| 5 | fitemid | 检查项id | varchar | 16 |  | √ | ' ' | 检查项id |
| 6 | ffgptasattachtemplateid | ai财务助手附件模板id或规则库id | int8 | 64 |  | √ | 0 | ai财务助手附件模板id或规则库id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_idi_fgptastemplatref |  | fid |
| 2 | idx_idi_fgptastemplatref |  | ffgptasattachtemplateid |
