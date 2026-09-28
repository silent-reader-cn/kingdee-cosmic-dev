# 定时任务设置-fsa_scheduletaskconfig

## 定时任务设置-主表 t_fsa_schtaskconfig

- **表名称：** 定时任务设置-主表
- **表名：** t_fsa_schtaskconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbydayorweek | 按日期或星期 | varchar | 4 |  | √ | ' ' | 按日期或星期,枚举: d :日期 w :星期 |
| 3 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fmonths | 选择的月份 | varchar | 50 |  | √ | ' ' | 选择的月份 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 8 | fweeks | 选择的星期 | varchar | 50 |  | √ | ' ' | 选择的星期 |
| 9 | fschid | 对应平台调度计划id | varchar | 36 |  | √ | ' ' | 对应平台调度计划id |
| 10 | fplan | cron表达式 | varchar | 300 |  | √ | ' ' | cron表达式 |
| 11 | fnoweek | 星期几 | varchar | 4 |  | √ | ' ' | 星期几,枚举: 1 :星期日 2 :星期一 3 :星期二 4 :星期三 5 :星期四 6 :星期五 7 :星期六 8 :自然日 9 :工作日 |
| 12 | fname | 定时任务名称 | varchar | 50 |  | √ | ' ' | 定时任务名称 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | fbyweek | 星期 | varchar | 1 |  | √ | ' ' | 星期 |
| 16 | fno | 第几个 | varchar | 4 |  | √ | ' ' | 第几个,枚举: 1 :第一个 2 :第二个 3 :第三个 4 :第四个 5 :第五个 L :最后一个 |
| 17 | frepeatmode | 任务执行时间单位 | varchar | 4 |  | √ | ' ' | 任务执行时间单位,枚举: n :不重复 mi :分钟 h :小时 d :天 w :星期 m :月 q :季度 y :年 def :自定义 |
| 18 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 19 | fdays | 选择的日期 | varchar | 100 |  | √ | ' ' | 选择的日期 |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | ftxtdesc | 调度计划示例 | varchar | 400 |  | √ | ' ' | 调度计划示例 |
| 22 | fnumber | 定时任务编码 | varchar | 50 |  | √ | ' ' | 定时任务编码 |
| 23 | fdesc | 描述 | varchar | 100 |  | √ | ' ' | 描述 |
| 24 | fendtime | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 25 | fcyclenum | 重复周期 | int4 | 32 |  | √ | 0 | 重复周期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fsa_sch_num |  | fnumber |
| 2 | pk_t_fsa_schtaskconfig |  | fid |

---

## 维度过滤条件分录-子表 t_fsa_schtasktimesub

- **表名称：** 维度过滤条件分录-子表
- **表名：** t_fsa_schtasktimesub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmemberjson | 成员信息json | varchar | 255 |  | √ | ' ' | 成员信息json |
| 2 | fdimnumber | 维度编码 | varchar | 50 |  | √ | ' ' | 维度编码 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdimname | 维度名称 | varchar | 50 |  | √ | ' ' | 维度名称 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | fmemberjson_tag | 成员信息json_详情 | text | 0 |  |  | null | 成员信息json_详情 |
| 8 | fsrcnumber | 源字段编码 | varchar | 50 |  | √ | ' ' | 源字段编码 |
| 9 | fdimmember | 维度成员 | varchar | 100 |  | √ | ' ' | 维度成员 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fsa_schtasktimesub |  | fdetailid |
| 2 | idx_fsa_schsub_id |  | fentryid |

---

## 任务设置分录-子表 t_fsa_schtaskentity

- **表名称：** 任务设置分录-子表
- **表名：** t_fsa_schtaskentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbatchparam | 批量生成必填参数 | varchar | 100 |  | √ | ' ' | 批量生成必填参数 |
| 3 | ftasktype | 任务类型 | varchar | 4 |  | √ | ' ' | 任务类型,枚举: 1 :取数任务 |
| 4 | ftasktext | 任务 | varchar | 50 |  | √ | ' ' | 任务 |
| 5 | fbatchparamjson_tag | 批量生成必填参数json_详情 | text | 0 |  |  | null | 批量生成必填参数json_详情 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | ftaskid | 任务id | varchar | 50 |  | √ | ' ' | 任务id |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fbatchparamjson | 批量生成必填参数json | varchar | 255 |  | √ | ' ' | 批量生成必填参数json |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fsa_schtask_id |  | fid |
| 2 | pk_t_fsa_schtaskentity |  | fentryid |

---

## 预计执行时间分录-子表 t_fsa_schtasktime

- **表名称：** 预计执行时间分录-子表
- **表名：** t_fsa_schtasktime

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fschtime | 预计执行时间 | timestamp | 0 |  |  | null | 预计执行时间 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fisexecuted | 是否已执行 | bpchar | 1 |  | √ | '0' | 是否已执行 |
| 6 | ftimestatus | 时间状态 | varchar | 4 |  | √ | ' ' | 时间状态,枚举: 0 :禁用 1 :启用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fsa_schtime_id |  | fid |
| 2 | pk_t_fsa_schtasktime |  | fentryid |

---

## 定时任务设置-多语言表 t_fsa_schtaskconfig_l

- **表名称：** 定时任务设置-多语言表
- **表名：** t_fsa_schtaskconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 定时任务名称 | varchar | 255 |  | √ | ' ' | 定时任务名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fsa_sch_l_fid |  | fid |
| 2 | pk_t_fsa_schtaskconfig_l |  | fpkid |

---

## 定时任务设置-分表 t_fsa_schtaskconfig_n

- **表名称：** 定时任务设置-分表
- **表名：** t_fsa_schtaskconfig_n

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmsgreceiver | 消息接收人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fssuccessnotify | 成功 | varchar | 1 |  | √ | ' ' | 成功 |
| 4 | fsmsgcontent | 消息内容 | varchar | 2000 |  | √ | ' ' | 消息内容 |
| 5 | fsnotifytype | 消息渠道 | varchar | 300 |  | √ | ' ' | 消息渠道,枚举: |
| 6 | fsfailnotify | 失败 | varchar | 1 |  | √ | ' ' | 失败 |
| 7 | fstimeout | 超时 | varchar | 1 |  | √ | ' ' | 超时 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fsa_schtaskconfig_n |  | fid |
| 2 | idx_fsa_sch_n_sn |  | fsnotifytype |
