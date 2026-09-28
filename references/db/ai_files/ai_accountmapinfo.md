# AI生成科目影响因素日志-ai_accountmapinfo

## AI生成科目影响因素日志-主表 t_ai_accountmapinfo

- **表名称：** AI生成科目影响因素日志-主表
- **表名：** t_ai_accountmapinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgptinput |  | varchar | 2000 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | faccountmaptype | 科目影响因素 | int8 | 64 |  | √ | 0 | [科目影响因素 ai_accountmaptype](../ai_files/ai_accountmaptype.md) |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'C' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fgptinput_tag | 详情 | text | 0 |  |  | null | 详情 |
| 8 | fgptoutput_tag | 详情 | text | 0 |  |  | null | 详情 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fgptoutput |  | varchar | 2000 |  | √ | ' ' |  |
| 13 | faccountrule | 科目核算规则 | int8 | 64 |  | √ | 0 | [科目核算规则 ai_account_rule](../ai_files/ai_account_rule.md) |
| 14 | faccounttype | 科目表 | int8 | 64 |  | √ | 0 | [科目表 bd_accounttable](../fibd_files/bd_accounttable.md) |
| 15 | faccountruleid | 科目核算规则id | varchar | 100 |  | √ | ' ' | 科目核算规则id |
| 16 | fmodelname | AI大模型 | varchar | 50 |  | √ | ' ' | AI大模型,枚举: TRIAL_BAIDU_ERNIE_BOT_PRO :免费试用AI大模型 AZURE_GPT_35 :Azure OpenAI Service: gpt-3.5-turbo AZURE_GPT_40 :Azure OpenAI Service: gpt-4.0 BAIDU_ERNIE_BOT :百度：文心一言 BAIDU_ERNIE_BOT_PRO :百度：文心一言 4.0 KINGDEE_FINANCE_GPT :金蝶: 财务大模型 DOUBAO_PRO_4K :豆包 pro 4k DOUBAO_PRO_32K :豆包 pro 32k DOUBAO_PRO_128K :豆包 pro 128k |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ai_accountmapinfo |  | fid |
| 2 | idx_ai_accountmapinfo_m0 |  | fbillno |
