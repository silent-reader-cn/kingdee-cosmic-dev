# 自动执行方案-sco_autoexecsheme

## 适用组织-子表 t_sco_autoexecorgentry

- **表名称：** 适用组织-子表
- **表名：** t_sco_autoexecorgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgid | 组织编码 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fcostaccountid | 成本主体编码 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fuserid | 消息接收人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_autoexecorgentry |  | fentryid |

---

## 自动执行方案-多语言表 t_sco_autoexecsheme_l

- **表名称：** 自动执行方案-多语言表
- **表名：** t_sco_autoexecsheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_autoexecsheme_l |  | fpkid |
| 2 | idx_sco_autoexecsheme_l |  | fid,flocaleid |

---

## 自动执行方案-主表 t_sco_autoexecsheme

- **表名称：** 自动执行方案-主表
- **表名：** t_sco_autoexecsheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fscheduleplan | 执行计划 | varchar | 1000 |  | √ | ' ' | 执行计划 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fappnum | 所属应用 | varchar | 10 |  | √ | ' ' | 所属应用 |
| 6 | fispreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fsheduleplanid | 调度计划id | varchar | 80 |  | √ | ' ' | 调度计划id |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 14 | fexecutorid | 执行人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_autoexecsheme |  | fid |
| 2 | idx_sco_autoexecsheme |  | fmasterid |

---

## 单据体-子表 t_sco_autoexecshemeentry

- **表名称：** 单据体-子表
- **表名：** t_sco_autoexecshemeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fbusinesstype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fautoexecoperid | 执行操作 | int8 | 64 |  | √ | 0 | 执行操作 sco_autoexecoper |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_autoexecshemeentry |  | fentryid |
| 2 | idx_sco_autoexecshemeentry |  | fid,fbusinesstype,fautoexecoperid |
