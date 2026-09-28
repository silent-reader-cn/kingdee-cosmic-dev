# 流程插件信息-wf_pluginprocinfo

## 流程插件信息-主表 t_wf_pluginprocinfo

- **表名称：** 流程插件信息-主表
- **表名：** t_wf_pluginprocinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexecutedtimes | 执行次数 | int4 | 32 |  | √ | 0 | 执行次数 |
| 3 | freferenceinfo | freferenceinfo | varchar | 2000 |  | √ | ' ' |  |
| 4 | fprocessno | 流程编码 | varchar | 50 |  | √ | ' ' | 流程编码 |
| 5 | fprocdefid | 流程定义id | int8 | 64 |  | √ | 0 | 流程定义id |
| 6 | fentitynumber | 单据实体编码 | varchar | 50 |  | √ | ' ' | 单据实体编码 |
| 7 | faverageduration | 平均耗时(s) | int8 | 64 |  | √ | 0 | 平均耗时(s) |
| 8 | ftotalduration | 总耗时(s) | int8 | 64 |  | √ | 0 | 总耗时(s) |
| 9 | fprocesstype | 流程类型 | varchar | 50 |  | √ | ' ' | 流程类型,枚举: AuditFlow :审批流 BizFlow :业务流 |
| 10 | felementid | 节点编码 | varchar | 255 |  | √ | ' ' | 节点编码 |
| 11 | fplugintype | 插件类型 | varchar | 50 |  | √ | ' ' | 插件类型,枚举: class :Java插件 script :ks脚本 operation :操作插件 |
| 12 | fpluginno | 插件编码 | varchar | 255 |  | √ | ' ' | 插件编码 |
| 13 | fscene | 场景 | varchar | 80 |  | √ | ' ' | 场景,枚举: CALCULATEPARTICIPANT :参与人 CONDITIONALRULE :条件规则 BILLSUBJECT :单据主题计算 TIMECONTROL :时限控制 CUSTOMAPPROVALRECORD :自定义审批记录数据源 PROCESS-PLUGIN :流程插件 START-NODE :进入节点时 LEAVE-NODE :离开节点时 HANDLE-TASK-NODE :任务处理时 NODE-PLUGIN :节点插件 |
| 14 | fprocnane | 流程名称 | varchar | 255 |  | √ | ' ' | 流程名称 |
| 15 | fentrabillname | 单据名称 | varchar | 255 |  | √ | ' ' | 单据名称 |
| 16 | fpluginname | 插件名称 | varchar | 500 |  | √ | ' ' | 插件名称 |
| 17 | fversion | 流程版本 | varchar | 36 |  | √ | ' ' | 流程版本 |
| 18 | felementname | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_wf_pluginprocinfo |  | fid |
| 2 | idx_wf_pluginprocinf_plugname |  | fpluginname |
| 3 | idx_wf_pluginprocinf_plugtype |  | fplugintype |
| 4 | idx_wf_pluginprocinf_procdef |  | fprocdefid |
| 5 | idx_wf_pluginprocinf_procplug |  | fprocessno,fpluginno |

---

## 流程插件信息-多语言表 t_wf_pluginprocinfo_l

- **表名称：** 流程插件信息-多语言表
- **表名：** t_wf_pluginprocinfo_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprocnane | 流程名称 | varchar | 255 |  | √ | ' ' | 流程名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fentrabillname | 单据名称 | varchar | 255 |  | √ | ' ' | 单据名称 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fpluginname | 插件名称 | varchar | 500 |  | √ | ' ' | 插件名称 |
| 7 | felementname | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_wf_pluginprocinfo_l |  | fpkid |
| 2 | idx_wf_pluginprocinfo_l |  | fid,flocaleid |
