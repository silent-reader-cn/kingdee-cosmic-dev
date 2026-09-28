# 自动执行方案-sca_autoexecsheme

## 单据体-子表 t_sca_autoexecshemeentry

- **表名称：** 单据体-子表
- **表名：** t_sca_autoexecshemeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fbusinesstype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: |
| 4 | fisvalid | 启用状态 | bpchar | 1 |  | √ | ' ' | 启用状态 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fautoexecoperid | 执行操作 | int8 | 64 |  | √ | 0 | 执行操作 sca_autoexecoper |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sca_autoexecshemeentry |  | fid,fbusinesstype,fautoexecoperid |
| 2 | pk_t_sca_autoexecshemeentry |  | fentryid |

---

## 自动执行方案-主表 t_sca_autoexecsheme

- **表名称：** 自动执行方案-主表
- **表名：** t_sca_autoexecsheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fscheduleplan | 执行计划 | varchar | 1000 |  | √ | ' ' | 执行计划 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fappnum | 所属应用 | varchar | 100 |  | √ | ' ' | 所属应用 |
| 6 | fispreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fsheduleplanid | 调度计划id | varchar | 50 |  | √ | ' ' | 调度计划id |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 14 | fexecutorid | 执行人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_autoexecsheme_pkey |  | fid |
| 2 | idx_sca_autoexecsheme |  | fmasterid |

---

## 适用成本主体-子表 t_sca_autoexecorgentry

- **表名称：** 适用成本主体-子表
- **表名：** t_sca_autoexecorgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgid | 核算组织编码 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fcostaccountid | 成本主体编码 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fuserid | 消息接收人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fcalcscheme | 成本计算方案 | int8 | 64 |  | √ | 0 | 查询方案 aca_calc_query_scheme |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_autoexecorgentry_pkey |  | fentryid |
| 2 | idx_autoexecorgentry |  | fid |

---

## 自动执行方案-多语言表 t_sca_autoexecsheme_l

- **表名称：** 自动执行方案-多语言表
- **表名：** t_sca_autoexecsheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sca_autoexecsheme_l |  | fid,flocaleid |
| 2 | t_sca_autoexecsheme_l_pkey |  | fpkid |
