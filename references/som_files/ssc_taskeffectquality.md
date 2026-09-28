# 共享任务时效质量统计表-ssc_taskeffectquality

## 共享任务时效质量统计表-主表 t_tk_sscagingquanlity

- **表名称：** 共享任务时效质量统计表-主表
- **表名：** t_tk_sscagingquanlity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 用户组 | int8 | 64 |  | √ | 0 | 用户组 task_usergroup |
| 3 | fspendtime | 共享耗时（小时） | numeric | 19 | 6 | √ | 0 | 共享耗时（小时） |
| 4 | ftasktype | 任务类型 | bpchar | 1 |  | √ | ' ' | 任务类型,枚举: 0 :初审 1 :复审 2 :质检 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | foverstdwork | 超期标准工作量 | numeric | 19 | 6 | √ | 0 | 超期标准工作量 |
| 11 | fovertasknum | 超期任务数 | int4 | 32 |  | √ | 0 | 超期任务数 |
| 12 | fisrecheck | 复审退回 | bpchar | 1 |  | √ | ' ' | 复审退回,枚举: 1 :未复审 2 :有复审且被退回 3 :有复审且未退回 |
| 13 | fsscid | 共享中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 15 | funqualifiedcount | 质检不合格次数 | int4 | 32 |  | √ | 0 | 质检不合格次数 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | ftasktypenew | 任务类型 | int8 | 64 |  | √ | 0 | 任务类型 task_tasktype |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fhandlerid | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fbillnumber | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 21 | fqualitycount | 被质检次数 | int4 | 32 |  | √ | 0 | 被质检次数 |
| 22 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 24 | ftaskid | 任务id | varchar | 30 |  | √ | ' ' | 任务id |
| 25 | ffirstaccesstime | 共享任务初次接收时间 | timestamp | 0 |  |  | null | 共享任务初次接收时间 |
| 26 | fcompletetime | 共享任务完成时间 | timestamp | 0 |  |  | null | 共享任务完成时间 |
| 27 | fcorrecttime | 校正后共享耗时(小时) | numeric | 19 | 6 | √ | 0 | 校正后共享耗时(小时) |
| 28 | fisoverdue | 是否超期 | bpchar | 1 |  | √ | ' ' | 是否超期,枚举: 0 :否 1 :是 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_sscagingquanlity |  | fsscid,ftaskid,fgroupid,fhandlerid,fcompletetime |
| 2 | pk_t_tk_sscagingquanlity |  | fid |

---

## 共享任务时效质量统计表-多语言表 t_tk_sscagingquanlity_l

- **表名称：** 共享任务时效质量统计表-多语言表
- **表名：** t_tk_sscagingquanlity_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 32 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_sscagingquanlity_l |  | fpkid |
| 2 | idx_ssc_sscagingqua_locale |  | fid,flocaleid |
