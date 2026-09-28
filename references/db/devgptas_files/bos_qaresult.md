# 问答反馈-bos_qaresult

## 单据体-子表 t_knl_qaresultentry

- **表名称：** 单据体-子表
- **表名：** t_knl_qaresultentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | ffilegroup | ffilegroup | int8 | 64 |  | √ | 0 |  |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | ffile | 知识名称 | int8 | 64 |  | √ | 0 | 苍穹智能问答 cosmicintelliqa |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_knl_qaresultentry |  | fid |
| 2 | pk_knl_qaresultentry |  | fentryid |

---

## 问答反馈-主表 t_knl_qaresult

- **表名称：** 问答反馈-主表
- **表名：** t_knl_qaresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fanswer | 回答 | varchar | 2000 |  | √ | ' ' | 回答 |
| 4 | fbillstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fassistant | 开发助手 | int8 | 64 |  | √ | 100000 | [开发助手 bos_corpus_assistant](../devgptas_files/bos_corpus_assistant.md) |
| 6 | fcreatetime | 上报时间 | timestamp | 0 |  |  | null | 上报时间 |
| 7 | ffdbkdesc | 反馈描述 | varchar | 200 |  | √ | ' ' | 反馈描述 |
| 8 | ffdbktype | 问题类型 | varchar | 200 |  | √ | ' ' | 问题类型,枚举: inaccuracy :内容不准确 slow :回答速度过慢 inconvenient :操作不方便 misinterpretation :答非所问 incomplete :内容不完整 incorrect :回答格式错误 |
| 9 | fclienttype | 客户端类型 | varchar | 50 |  | √ | ' ' | 客户端类型,枚举: 1 :Web端 2 :IDEA 3 :VSCode 99 :其他 4 :苍穹 |
| 10 | fnote | 备注说明 | varchar | 2000 |  | √ | ' ' | 备注说明 |
| 11 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | fuserinput_tag | 用户输入_详情 | text | 0 |  |  | null | 用户输入_详情 |
| 13 | fanswer_tag | 回答_详情 | text | 0 |  |  | null | 回答_详情 |
| 14 | fchatsessionid | 对话id | varchar | 200 |  | √ | ' ' | 对话id |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fcreatorid | 用户信息 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fuserinput | 用户输入 | varchar | 2000 |  | √ | ' ' | 用户输入 |
| 18 | ftype | 反馈类型 | varchar | 50 |  | √ | ' ' | 反馈类型,枚举: A :未匹配 B :赞 C :踩 D :正常 E :异常 F :手动终止 |
| 19 | fgroup | 所属模块 | int8 | 64 |  | √ | 0 | [知识分组 knl_group](../devgptas_files/knl_group.md) |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fformid | 上报来源 | varchar | 200 |  | √ | ' ' | 上报来源 |
| 22 | fanalyse | 详细类别 | int8 | 64 |  | √ | 0 | [反馈分析类型 bos_qaresultanalyse](../devgptas_files/bos_qaresultanalyse.md) |
| 23 | fgrouptype | 应用助手 | int8 | 64 |  | √ | 0 | [知识管理 corpus_libs](../devgptas_files/corpus_libs.md) |
| 24 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_knl_qaresult |  | fid |
| 2 | idx_knl_qaresult |  | fbillno |
| 3 | idx_knl_qaresouice_chatsession |  | fchatsessionid |
