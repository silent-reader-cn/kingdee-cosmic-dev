# 信用变更日志-task_creditmodifylog

## 信用变更日志-多语言表 t_tk_creditmodifylog_l

- **表名称：** 信用变更日志-多语言表
- **表名：** t_tk_creditmodifylog_l

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
| 1 | t_tk_creditmodifylog_l_pkey |  | fpkid |
| 2 | indx_ssc_fid_crdmdlg_l |  | fid,flocaleid |

---

## 信用变更日志-主表 t_tk_creditmodifylog

- **表名称：** 信用变更日志-主表
- **表名：** t_tk_creditmodifylog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 3 | fnewlevel | 变更后等级 | varchar | 50 |  | √ | ' ' | 变更后等级 |
| 4 | fcompany | 公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | ftaskid_link | 历史任务id_超链接 | int8 | 64 |  | √ | 0 | 历史任务id_超链接 |
| 6 | fiscancel | 是否已撤回 | bpchar | 1 |  | √ | '0' | 是否已撤回 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fnewgrade | 变更后分数 | numeric | 19 | 6 | √ | 0.000000 | 变更后分数 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fmodifydate | 变更时间 | timestamp | 0 |  |  | null | 变更时间 |
| 13 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 14 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 15 | fbillentity | 单据标识 | varchar | 30 |  | √ | ' ' | 单据标识 |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fraiser | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fmodifysource | 变更来源 | bpchar | 1 |  | √ | ' ' | 变更来源,枚举: 0 :初始化 1 :手动修改 2 :审核 3 :影像超期 4 :共享质检任务 5 :信用申诉 |
| 22 | fchangedscore | 分数变化 | numeric | 19 | 6 | √ | 0.000000 | 分数变化 |
| 23 | fdept | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 24 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 25 | foldlevel | 原等级 | varchar | 50 |  | √ | ' ' | 原等级 |
| 26 | fctrlstrategy | fctrlstrategy | varchar | 30 |  | √ | ' ' |  |
| 27 | fbilltopic | 单据主题 | varchar | 255 |  | √ | ' ' | 单据主题 |
| 28 | fmodifytype | 变更类型 | bpchar | 1 |  | √ | ' ' | 变更类型,枚举: 1 :升级 2 :降级 3 :加分 4 :减分 |
| 29 | fbillid | 单据id | varchar | 32 |  | √ | ' ' | 单据id |
| 30 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 31 | foldgrade | 原分数 | numeric | 19 | 6 | √ | 0.000000 | 原分数 |
| 32 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 33 | ftaskid | 历史任务id | int8 | 64 |  | √ | 0 | 历史任务id |
| 34 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_tk_cretmodlog_fmoddate |  | fmodifydate |
| 2 | t_tk_creditmodifylog_pkey |  | fid |
| 3 | index_tk_cretmodlog_fraiser |  | fraiser |
| 4 | idx_t_tk_creditmodifylog_createorg |  | fcreateorgid |
| 5 | idx_t_tk_creditmodifylog_master |  | fmasterid |
| 6 | index_cretmodlog_fcrateorgid |  | fcreateorgid |
| 7 | index_tk_cretmodlog_fdept |  | fdept |
| 8 | index_tk_cretmodlog_taskid |  | ftaskid |
| 9 | index_tk_cretmodlog_fmodtype |  | fmodifytype |
| 10 | index_tk_cretmodlog_fcompany |  | fcompany |
