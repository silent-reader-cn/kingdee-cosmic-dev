# DAP配置-ai_dapconfig

## DAP配置-主表 t_ai_dapconfig

- **表名称：** DAP配置-主表
- **表名：** t_ai_dapconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparentbillid | 公共单 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | foper | 关联操作 | varchar | 50 |  | √ | ' ' | 关联操作 |
| 4 | fentrysum | 分录汇总 | bpchar | 1 |  | √ | '0' | 分录汇总 |
| 5 | fisdap | 参与生成凭证 | bpchar | 1 |  | √ | ' ' | 参与生成凭证 |
| 6 | fisselecttemp | 启用凭证多规则 | bpchar | 1 |  | √ | '0' | 启用凭证多规则 |
| 7 | fhasvchfldname | 已生成凭证字段名称 | varchar | 50 |  | √ | ' ' | 已生成凭证字段名称 |
| 8 | fwritebackplugin | 反写插件 | varchar | 400 |  |  | ' ' | 反写插件 |
| 9 | fsavebizvoucherentry | 保存业务凭证分录 | bpchar | 1 |  | √ | ' ' | 保存业务凭证分录 |
| 10 | fonlygetdata | 作为关联单据不生成凭证 | bpchar | 1 |  | √ | ' ' | 作为关联单据不生成凭证 |
| 11 | fbillentity | 单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 12 | fcustomuniquekey | 自定义唯一标识 | varchar | 100 |  | √ | ' ' | 自定义唯一标识 |
| 13 | feventclassid | 事件 | int8 | 64 |  | √ | 0 | [异构数据对接模型 ai_eventclass](../ai_files/ai_eventclass.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_dapconfig_bill |  | fbillentity,feventclassid |
| 2 | t_ai_dapconfig_pkey |  | fid |
