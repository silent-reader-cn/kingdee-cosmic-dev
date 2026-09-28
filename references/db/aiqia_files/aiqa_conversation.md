# AI报价会话-aiqa_conversation

## 单据体-子表 t_aiqa_conversation_me

- **表名称：** 单据体-子表
- **表名：** t_aiqa_conversation_me

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmessage | 消息内容 | varchar | 255 |  | √ | ' ' | 消息内容 |
| 3 | fparentid | 父级消息id | int8 | 64 |  | √ | 0 | 父级消息id |
| 4 | fclarify | 下一步是否澄清 | bpchar | 1 |  | √ | '0' | 下一步是否澄清 |
| 5 | fmessagetime | 消息时间 | timestamp | 0 |  |  | null | 消息时间 |
| 6 | fprocessid | 澄清工作流id | varchar | 50 |  | √ | ' ' | 澄清工作流id |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | ffileurl | 文件地址 | varchar | 500 |  | √ | ' ' | 文件地址 |
| 9 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fclarifytype | 澄清类型 | varchar | 50 |  | √ | ' ' | 澄清类型 |
| 12 | foperatetype | 操作类型 | varchar | 50 |  | √ | ' ' | 操作类型 |
| 13 | fsessionid | 澄清工作流会话id | varchar | 50 |  | √ | ' ' | 澄清工作流会话id |
| 14 | fmessagetype | 对话类型 | varchar | 50 |  | √ | ' ' | 对话类型,枚举: |
| 15 | fokorno | 赞踩 | varchar | 50 |  | √ | ' ' | 赞踩 |
| 16 | fusertype | 发言人类型 | varchar | 50 |  | √ | ' ' | 发言人类型 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fmessage_tag | 消息内容_详情 | text | 0 |  |  | null | 消息内容_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aiqa_conversation_me_fk |  | fid |
| 2 | pk_aiqa_conversation_me |  | fentryid |

---

## AI报价会话-主表 t_aiqa_conversation

- **表名称：** AI报价会话-主表
- **表名：** t_aiqa_conversation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 会话名 | varchar | 50 |  | √ | ' ' | 会话名 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcustomername | 客户名称 | varchar | 1000 |  | √ | ' ' | 客户名称 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fcursessionid | 当前工作流sessionid | varchar | 50 |  | √ | ' ' | 当前工作流sessionid |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fprequoteid | 报价单 | int8 | 64 |  | √ | 0 | 预报价单 aiqa_prequote |
| 11 | fpageid | 最后打开页面的pageid | varchar | 100 |  | √ | ' ' | 最后打开页面的pageid |
| 12 | fmessagestatus | 会话状态 | varchar | 50 |  | √ | ' ' | 会话状态,枚举: A :选择客户 B :填充物料清单 C :已完成 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fupdatetime | 修改时间 | int4 | 32 |  | √ | '-1' | 修改时间 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aiqa_conversation_m0 |  | fbillno |
| 2 | pk_aiqa_conversation |  | fid |
