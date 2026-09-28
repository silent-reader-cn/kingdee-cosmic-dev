# 业务单据-task_taskbill

## 字段映射-子表 t_tk_fieldmapentry

- **表名称：** 字段映射-子表
- **表名：** t_tk_fieldmapentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldconfiguration | 任务字段名称 | varchar | 80 |  | √ | ' ' | 任务字段名称,枚举: 10 :组织 20 :申请人 30 :提单日期 40 :承担部门 50 :费用项目 60 :报销金额 70 :供应商 80 :任务量系数因子 |
| 3 | fsourcefieldname | 单据字段名称 | varchar | 80 |  | √ | ' ' | 单据字段名称 |
| 4 | fsourcefieldnumber | 单据字段编码 | varchar | 80 |  | √ | ' ' | 单据字段编码 |
| 5 | ftype | 类型 | bpchar | 1 |  | √ | ' ' | 类型,枚举: 0 :字符串 1 :日期 2 :数字 3 :日期时间 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fdynamicfield | 动态字段主键 | int8 | 64 |  | √ | 0 | 动态字段主键 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_fieldmapentry_fid |  | fid |
| 2 | t_tk_fieldmapentry_pkey |  | fentryid |

---

## 单据体-子表 t_tk_taskrulebill

- **表名称：** 单据体-子表
- **表名：** t_tk_taskrulebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftasktype | 任务类型 | int8 | 64 |  | √ | 0 | [任务类型 task_tasktype](../ssc_files/task_tasktype.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fchildpkid | 长整数 | int8 | 64 |  | √ | 0 | 长整数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_taskrulebill_pkey |  | fentryid |
| 2 | index_taskrulebill |  | fid |

---

## 业务单据-主表 t_tk_taskmainbill

- **表名称：** 业务单据-主表
- **表名：** t_tk_taskmainbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsscid | 共享中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fbindbill | 来源单据 | varchar | 50 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | frelationtype | 委托关系类型 | varchar | 8 |  | √ | ' ' | 委托关系类型,枚举: 1 :核算组织委托共享中心 |
| 7 | fdescription | 描述 | varchar | 255 |  |  | null | 描述 |
| 8 | fbindform | 绑定展示界面 | varchar | 50 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |
| 9 | fisembed | 是否为嵌入单据 | bpchar | 1 |  | √ | '0' | 是否为嵌入单据 |
| 10 | fisneedvoucher | 共享生成凭证 | bpchar | 1 |  | √ | '0' | 共享生成凭证 |
| 11 | fispartask | 是否为多级任务 | bpchar | 1 |  | √ | '0' | 是否为多级任务 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fisneedimage | 需要影像上传 | bpchar | 1 |  | √ | '0' | 需要影像上传 |
| 17 | fisstoredindb | 单据数据是否存表 | bpchar | 1 |  | √ | '0' | 单据数据是否存表 |
| 18 | feffective | 生效状态 | bpchar | 1 |  | √ | '1' | 生效状态,枚举: 0 :失效 1 :生效 |
| 19 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fexternalerpid | 所属系统 | int8 | 64 |  | √ | 0 | [业务系统 bas_extenderp](../sys_files/bas_extenderp.md) |
| 21 | fbilloperationconfig | 审批调用操作配置 | varchar | 50 |  | √ | ' ' | 审批调用操作配置 |
| 22 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 23 | fautosynorg | 自动同步适用组织 | bpchar | 1 |  | √ | '0' | 自动同步适用组织,枚举: 0 :否 1 :是 |
| 24 | fuselang | 使用语言-隐藏、默认用户当前设置的语言 | varchar | 10 |  | √ | ' ' | 使用语言-隐藏、默认用户当前设置的语言,枚举: zh_CN :简体中文 en_US :English zh_TW :繁體中文 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_ssc_taskmainbill |  | fnumber |
| 2 | t_tk_taskmainbill_pkey |  | fid |

---

## 适用组织-多选基础资料表 t_tk_sscbillorg

- **表名称：** 适用组织-多选基础资料表
- **表名：** t_tk_sscbillorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_sscbillorg_pkey |  | fpkid |
| 2 | idx_ssc_sscbillorg |  | fbasedataid |

---

## 业务单据-多语言表 t_tk_taskmainbill_l

- **表名称：** 业务单据-多语言表
- **表名：** t_tk_taskmainbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_ssc_taskmainbill_l |  | fid,flocaleid |
| 2 | t_tk_taskmainbill_l_pkey |  | fpkid |
