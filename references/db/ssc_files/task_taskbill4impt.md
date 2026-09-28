# 业务单据（引入）-task_taskbill4impt

## 业务单据（引入）-多语言表 t_tk_taskbill4impt_l

- **表名称：** 业务单据（引入）-多语言表
- **表名：** t_tk_taskbill4impt_l

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
| 1 | pk_t_tk_taskbill4impt_l |  | fpkid |
| 2 | idx_taskbill4impt_l_fid |  | fid,flocaleid |

---

## 业务单据（引入）-主表 t_tk_taskbill4impt

- **表名称：** 业务单据（引入）-主表
- **表名：** t_tk_taskbill4impt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisisomer | fisisomer | bpchar | 1 |  | √ | '0' |  |
| 3 | frelationtype | 委托关系类型 | varchar | 8 |  | √ | ' ' | 委托关系类型,枚举: 1 :核算组织委托共享中心 |
| 4 | fisneedvoucher | 共享生成凭证 | bpchar | 1 |  | √ | '0' | 共享生成凭证 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fisstoredindb | 单据数据是否存表 | bpchar | 1 |  | √ | '0' | 单据数据是否存表 |
| 10 | fexternalerpid | 所属系统 | int8 | 64 |  | √ | 0 | 业务系统 bas_extenderp |
| 11 | fautosynorg | 自动同步适用组织 | bpchar | 1 |  | √ | '0' | 自动同步适用组织,枚举: 0 :否 1 :是 |
| 12 | fsscid | 共享中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fbindbill | 来源单据 | varchar | 50 |  | √ | ' ' | 表单元数据 bos_formmeta |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 17 | fbindform | 绑定展示界面 | varchar | 50 |  | √ | ' ' | 表单元数据 bos_formmeta |
| 18 | fisembed | 是否为嵌入单据 | bpchar | 1 |  | √ | '0' | 是否为嵌入单据 |
| 19 | fisomertasktype | fisomertasktype | int8 | 64 |  | √ | 0 |  |
| 20 | fispartask | 是否为多级任务 | bpchar | 1 |  | √ | '0' | 是否为多级任务 |
| 21 | fisautoopenimage | fisautoopenimage | bpchar | 1 |  | √ | '0' |  |
| 22 | fisneedimage | 需要影像上传 | bpchar | 1 |  | √ | '0' | 需要影像上传 |
| 23 | feffective | 生效状态 | bpchar | 1 |  | √ | '1' | 生效状态,枚举: 0 :失效 1 :生效 |
| 24 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 26 | fuselang | 使用语言-隐藏、默认用户当前设置的语言 | varchar | 10 |  | √ | ' ' | 使用语言-隐藏、默认用户当前设置的语言,枚举: zh_CN :简体中文 en_US :English zh_TW :繁體中文 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_taskbill4impt |  | fid |
| 2 | idx_taskbill4impt_number |  | fnumber |
| 3 | idx_taskbill4impt_bindbill |  | fbindbill |
