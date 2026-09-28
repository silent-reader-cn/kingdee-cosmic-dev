# 业务单据-子页面-task_taskbill_child

## 单据体-检查项-子表 t_tk_checkconditionentry

- **表名称：** 单据体-检查项-子表
- **表名：** t_tk_checkconditionentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fcheckrule | 自动检查规则 | varchar | 80 |  | √ | ' ' | 自动检查规则 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | ftaskcheckid | 检查项 | int8 | 64 |  | √ | 0 | [人工检查项 task_checkpoint](../ssc_files/task_checkpoint.md) |
| 6 | fchecktype | 类型 | bpchar | 1 |  | √ | '0' | 类型,枚举: 0 :自动 1 :手动 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_checkconditionentry_pkey |  | fentryid |
| 2 | index_ssc_checkconditionentry |  | fid |

---

## 业务单据-子页面-主表 t_tk_taskbillchild

- **表名称：** 业务单据-子页面-主表
- **表名：** t_tk_taskbillchild

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexecuteoprt | 执行操作 | varchar | 50 |  | √ | ' ' | 执行操作 |
| 3 | fautodecision | 智能检查项方案配置 | int8 | 64 |  | √ | 0 | [决策方案 idi_schema](../idi_files/idi_schema.md) |
| 4 | fissame | 与前置任务处理人不同 | bpchar | 1 |  | √ | '0' | 与前置任务处理人不同 |
| 5 | ftaskcount | 最大分配任务条数 | int8 | 64 |  | √ | 0 | 最大分配任务条数 |
| 6 | ftasktypeid | 任务类型 | int8 | 64 |  | √ | 0 | [任务类型 task_tasktype](../ssc_files/task_tasktype.md) |
| 7 | fbillattriconfigjson_tag | 单据修改权限配置json_详情 | text | 0 |  |  | null | 单据修改权限配置json_详情 |
| 8 | fimagenumgenoprtnumber | 影像编码生成节点编码 | varchar | 50 |  | √ | ' ' | 影像编码生成节点编码 |
| 9 | fisvoucherhandler | 共享处理人为凭证制单人 | bpchar | 1 |  | √ | '0' | 共享处理人为凭证制单人 |
| 10 | fexecuteoprtnumber | 执行操作编码 | varchar | 50 |  | √ | ' ' | 执行操作编码 |
| 11 | ftaskoprt | 任务触发操作 | varchar | 50 |  | √ | ' ' | 任务触发操作 |
| 12 | ftaskhour | 预警时间(小时) | numeric | 23 | 10 | √ | 0.0000000000 | 预警时间(小时) |
| 13 | ftasksubjectid | 任务主题ID | int8 | 64 |  | √ | 0 | 任务主题ID |
| 14 | ftaskoriginal | 任务来源 | bpchar | 1 |  | √ | '0' | 任务来源,枚举: 0 :工作流 1 :操作 2 :多级任务 |
| 15 | freverseoprt | 反向操作 | varchar | 50 |  | √ | ' ' | 反向操作 |
| 16 | fisintelldecision | 是否启用小K洞察 | bpchar | 1 |  | √ | '0' | 是否启用小K洞察 |
| 17 | ftasksubject | 任务主题 | varchar | 500 |  | √ | ' ' | 任务主题 |
| 18 | fchildssc | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fneedimage | 是否需要影像上传 | bpchar | 1 |  | √ | '0' | 是否需要影像上传 |
| 20 | fbillattriconfigjson | 单据修改权限配置json | varchar | 128 |  | √ | ' ' | 单据修改权限配置json |
| 21 | ftaskoprtnumber | 任务触发操作编码 | varchar | 50 |  | √ | ' ' | 任务触发操作编码 |
| 22 | freverseoprtnumber | 反向操作编码 | varchar | 50 |  | √ | ' ' | 反向操作编码 |
| 23 | fpretasktypeid | 前置触发任务 | int8 | 64 |  | √ | 0 | [任务类型 task_tasktype](../ssc_files/task_tasktype.md) |
| 24 | fimagenumgenoprt | 创建影像编码节点 | varchar | 50 |  | √ | ' ' | 创建影像编码节点 |
| 25 | fnexttasks | 后置任务 | varchar | 100 |  | √ | ' ' | 后置任务 |
| 26 | fbillattriconfig | 单据权限配置 | varchar | 2000 |  | √ | ' ' | 单据权限配置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_taskbillchild_pkey |  | fid |
| 2 | index_ssc_taskbillchild |  | ftasktypeid |

---

## 凭证处理单据体-子表 t_tk_voucherhandle

- **表名称：** 凭证处理单据体-子表
- **表名：** t_tk_voucherhandle

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillconditionjson | 单据条件json | varchar | 255 |  | √ | ' ' | 单据条件json |
| 3 | fvoucheroperation | 任务对应完成凭证操作 | bpchar | 1 |  | √ | ' ' | 任务对应完成凭证操作,枚举: 1 :不处理凭证 2 :生成凭证 3 :提交凭证 4 :审核凭证 |
| 4 | ftaskhandleshowtext | 任务处理显示操作 | varchar | 100 |  | √ | ' ' | 任务处理显示操作 |
| 5 | fbillconditionjson_tag | 单据条件json_详情 | text | 0 |  |  | null | 单据条件json_详情 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fbillcondition | 单据条件 | varchar | 1000 |  | √ | ' ' | 单据条件 |
| 8 | fvoucherstatctrl | 提交任务受凭证状态控制 | bpchar | 1 |  | √ | ' ' | 提交任务受凭证状态控制,枚举: 1 :不控制 2 :弱控制 3 :强控制 |
| 9 | ftaskhandleshow | 任务处理显示操作下拉框 | varchar | 50 |  | √ | ' ' | 任务处理显示操作下拉框,枚举: 1 :预览凭证 2 :查看凭证 3 :生成凭证 4 :删除凭证 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_voucherhandle |  | fentryid |
| 2 | idx_t_tk_voucherhandle_fk |  | fid |

---

## 单据体-优先级-子表 t_tk_levelentry

- **表名称：** 单据体-优先级-子表
- **表名：** t_tk_levelentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftimeliness | 时效（小时） | numeric | 23 | 10 | √ | 0.0000000000 | 时效（小时） |
| 3 | fpriorityrule | 满足优先级的条件 | varchar | 2000 |  | √ | ' ' | 满足优先级的条件 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fwarningtime | 预警时间（小时） | numeric | 10 | 2 | √ | 0.00 | 预警时间（小时） |
| 6 | fpriorityid | 优先级 | int8 | 64 |  | √ | 0 | [任务优先级 task_tasklevel](../ssc_files/task_tasklevel.md) |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fpriorityrulejson | 满足优先级的条件Json | text | 0 |  |  | null | 满足优先级的条件Json |
| 9 | fpriorityrulejson_tag | 满足优先级的条件Json_详情 | text | 0 |  |  | null | 满足优先级的条件Json_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_ssc_levelentry |  | fid |
| 2 | t_tk_levelentry_pkey |  | fentryid |

---

## 前置任务-多选基础资料表 t_tk_pretask

- **表名称：** 前置任务-多选基础资料表
- **表名：** t_tk_pretask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [任务类型 task_tasktype](../ssc_files/task_tasktype.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_pretask_pkey |  | fpkid |
| 2 | index_ssc_pretaskid |  | fid |

---

## 单据体-过滤-子表 t_tk_filterconditionentry

- **表名称：** 单据体-过滤-子表
- **表名：** t_tk_filterconditionentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldnumber | 字段编码 | varchar | 50 |  | √ | ' ' | 字段编码 |
| 3 | fvalue | 值 | varchar | 50 |  | √ | ' ' | 值 |
| 4 | ffieldname | 字段 | varchar | 50 |  | √ | ' ' | 字段 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | frelation | 逻辑 | bpchar | 1 |  | √ | '0' | 逻辑,枚举: 0 :AND 1 :OR |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fcomparesign | 比较符 | bpchar | 1 |  | √ | '0' | 比较符,枚举: 0 :> 1 :< 2 := 3 :!= 4 :>= 5 :<= |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_filterconditionentry_pkey |  | fentryid |
| 2 | index_ssc_filterconditionentry |  | fid |

---

## 小K洞察配置-多选基础资料表 t_tk_idischemaconf

- **表名称：** 小K洞察配置-多选基础资料表
- **表名：** t_tk_idischemaconf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [决策方案 idi_schema](../idi_files/idi_schema.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_idischemaconf_pkey |  | fpkid |
| 2 | idx_ssc_idischemaconf_fbdid |  | fbasedataid |

---

## 人工检查项配置-多选基础资料表 t_tk_articheckpointconfig

- **表名称：** 人工检查项配置-多选基础资料表
- **表名：** t_tk_articheckpointconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人工检查项 task_checkpoint](../ssc_files/task_checkpoint.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_checkpointconfig_bdt |  | fbasedataid |
| 2 | pk_t_tk_articheckpointconfig |  | fpkid |
| 3 | idx_ssc_checkpointconfig_id |  | fid |
