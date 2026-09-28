# 流程预计算实例-wf_precomputorinstance

## 流程预计算实例-主表 t_wf_precomputorinstance

- **表名称：** 流程预计算实例-主表
- **表名：** t_wf_precomputorinstance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fentrynodeid | 入口节点ID | varchar | 255 |  | √ | ' ' | 入口节点ID |
| 3 | fentrytaskid | 入口任务ID | int8 | 64 |  | √ | 0 | 入口任务ID |
| 4 | fexecutionid | 执行实例ID | int8 | 64 |  | √ | 0 | 执行实例ID |
| 5 | fschemeid | 方案id | int8 | 64 |  | √ | 0 | 方案id |
| 6 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 7 | fstrategy | 更新策略 | varchar | 30 |  | √ | ' ' | 更新策略,枚举: through :流转 viewflowchart :查看流程图 |
| 8 | fentryauditname | 入口节点决策名称 | varchar | 50 |  | √ | ' ' | 入口节点决策名称 |
| 9 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 10 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 11 | factid | 当前活动节点ID | varchar | 2000 |  | √ | ' ' | 当前活动节点ID |
| 12 | fentryauditnumber | 入口节点决策项 | varchar | 50 |  | √ | ' ' | 入口节点决策项 |
| 13 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fvalidity | 有效性 | bpchar | 1 |  | √ | '0' | 有效性 |
| 15 | factivityname | 当前节点 | varchar | 2000 |  | √ | ' ' | 当前节点 |
| 16 | fbusinesskey | 业务主键 | varchar | 36 |  | √ | ' ' | 业务主键 |
| 17 | fentrynodename | 入口节点 | varchar | 500 |  | √ | ' ' | 入口节点 |
| 18 | fversion | 版本 | int8 | 64 |  | √ | 0 | 版本 |
| 19 | fbillno | 单据编码 | varchar | 255 |  | √ | ' ' | 单据编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idk_wf_precompinst_procver |  | fprocinstid,fversion |
| 2 | idk_wf_precompinst_scheme |  | fschemeid |
| 3 | idk_wf_precompinst_validity |  | fvalidity |
| 4 | pk_t_wf_precomputorinstance |  | fid |

---

## 预计算结果集-子表 t_wf_precomputorresult

- **表名称：** 预计算结果集-子表
- **表名：** t_wf_precomputorresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexceptionmsg | 异常信息 | varchar | 2000 |  | √ | ' ' | 异常信息 |
| 3 | fnodetype | 节点类型 | varchar | 100 |  | √ | ' ' | 节点类型 |
| 4 | fisnormal | 节点状态 | bpchar | 1 |  | √ | '1' | 节点状态 |
| 5 | fbizidentifykey | 业务标识 | varchar | 255 |  | √ | ' ' | 业务标识 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | ferrtype | 错误类型 | varchar | 50 |  | √ | ' ' | 错误类型,枚举: multioutedge :多出口线 noneoutedge :无出口线 missinedge :汇聚节点缺入口线 rulecalculate :条件规则计算出错 |
| 8 | fassignee | 参与人 | varchar | 2000 |  | √ | ' ' | 参与人 |
| 9 | fstatus | 处理类型 | varchar | 50 |  | √ | ' ' | 处理类型,枚举: skip :跳过 byAuto :自动流转 autonode :自动审批 through :审批 |
| 10 | fassigneename | 参与人名称 | varchar | 2000 |  | √ | ' ' | 参与人名称 |
| 11 | fnodename | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |
| 12 | ferrmsg | 错误信息 | varchar | 2000 |  | √ | ' ' | 错误信息 |
| 13 | fnodeid | 节点id | varchar | 255 |  | √ | ' ' | 节点id |
| 14 | fnextnodeid | 下一步节点 | varchar | 2000 |  | √ | ' ' | 下一步节点 |
| 15 | fauditnumber | 决策结果 | varchar | 50 |  | √ | ' ' | 决策结果 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fexceptionmsg_tag | 异常信息_详情 | text | 0 |  |  | null | 异常信息_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_wf_precomputorresult |  | fentryid |
| 2 | idx_wf_precomputorresult |  | fid |

---

## 流程预计算实例-多语言表 t_wf_precomputorinstance_l

- **表名称：** 流程预计算实例-多语言表
- **表名：** t_wf_precomputorinstance_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | factivityname | 当前节点 | varchar | 2000 |  | √ | ' ' | 当前节点 |
| 3 | fentrynodename | 入口节点 | varchar | 500 |  | √ | ' ' | 入口节点 |
| 4 | fentryauditname | 入口节点决策名称 | varchar | 50 |  | √ | ' ' | 入口节点决策名称 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idk_wf_precomputorinst_l |  | fid,flocaleid |
| 2 | pk_t_wf_precomputorinstance_l |  | fpkid |

---

## 预计算结果集-多语言表 t_wf_precomputorresult_l

- **表名称：** 预计算结果集-多语言表
- **表名：** t_wf_precomputorresult_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassigneename | 参与人名称 | varchar | 2000 |  | √ | ' ' | 参与人名称 |
| 3 | fnodename | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |
| 4 | ferrmsg | 错误信息 | varchar | 2000 |  | √ | ' ' | 错误信息 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_precomputorresult_l |  | fid,flocaleid |
| 2 | pk_t_wf_precomputorresult_l |  | fpkid |
