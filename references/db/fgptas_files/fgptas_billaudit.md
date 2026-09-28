# 附件审核-fgptas_billaudit

## 附件审核-主表 t_fgptas_audit

- **表名称：** 附件审核-主表
- **表名：** t_fgptas_audit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 2 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fgairepo | 知识库 | int8 | 64 |  | √ | 0 | [知识库 gai_repo_info](../gai_files/gai_repo_info.md) |
| 6 | fconfigtime | 配置时间 | timestamp | 0 |  |  | null | 配置时间 |
| 7 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fentityobject | 实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 9 | foutput | 审核要素总结内容 | varchar | 255 |  | √ | ' ' | 审核要素总结内容 |
| 10 | fruntimestatus | 实时状态 | varchar | 2 |  | √ | ' ' | 实时状态,枚举: 0 :新建 1 :向量化处理中 2 :附件审核处理中 3 :成功 4 :无附件 5 :GPT调用异常 6 :附件审核配置异常 7 :向量化失败 |
| 11 | felement | 审核要素 | varchar | 1000 |  | √ | ' ' | 审核要素 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | foutput_tag | 审核要素总结内容_详情 | text | 0 |  |  | null | 审核要素总结内容_详情 |
| 14 | fentityid | 实体ID | int8 | 64 |  | √ | 0 | 实体ID |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fgptas_audit_entity |  | fentityobject |
| 2 | idx_fgptas_audit_entity_id |  | fentityid |
| 3 | pk_t_fgptas_audit |  | fid |
