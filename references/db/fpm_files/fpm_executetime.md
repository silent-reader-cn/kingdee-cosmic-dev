# 控制执行时机配置（废弃）-fpm_executetime

## 预占单据体-子表 t_fpm_preemptedtime

- **表名称：** 预占单据体-子表
- **表名：** t_fpm_preemptedtime

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | funpreemptedcode | 取消预占时机编码 | varchar | 1024 |  | √ | ' ' | 取消预占时机编码 |
| 3 | fpreemptedtimecode | 预占时机编码 | varchar | 1024 |  | √ | ' ' | 预占时机编码 |
| 4 | frelease | 释放预占时机 | varchar | 1024 |  | √ | ' ' | 释放预占时机 |
| 5 | freleasecode | 释放预占时机编码 | varchar | 1024 |  | √ | ' ' | 释放预占时机编码 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | funpreempted | 取消预占时机 | varchar | 1024 |  | √ | ' ' | 取消预占时机 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fpreemptedtime | 预占时机 | varchar | 1024 |  | √ | ' ' | 预占时机 |
| 10 | fbusinessbillid | 业务单据 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fpm_preemptedtime |  | fid |
| 2 | pk_t_fpm_preemptedtime |  | fentryid |

---

## 控制执行时机配置（废弃）-主表 t_fpm_executetime

- **表名称：** 控制执行时机配置（废弃）-主表
- **表名：** t_fpm_executetime

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 5 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 6 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | ftimelimit | 可自动释放的预占期限（天） | int4 | 32 |  | √ | 0 | 可自动释放的预占期限（天） |
| 8 | fbodysysid | 体系 | int8 | 64 |  | √ | 0 | [体系管理1（废弃） fpm_bodysysmanage](../fpm_files/fpm_bodysysmanage.md) |
| 9 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 10 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fautorelease | 长期未扣减预占自动释放 | bpchar | 1 |  | √ | '0' | 长期未扣减预占自动释放 |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fpm_executetime |  | fbodysysid |
| 2 | pk_t_fpm_executetime |  | fid |

---

## 关联预占的业务单据-多选基础资料表 t_fpm_preemptedbill

- **表名称：** 关联预占的业务单据-多选基础资料表
- **表名：** t_fpm_preemptedbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fpm_preemptedbill |  | fentryid |
| 2 | pk_t_fpm_preemptedbill |  | fpkid |

---

## 实占（实际扣减）的业务单据-多选基础资料表 t_fpm_acldeductionbill

- **表名称：** 实占（实际扣减）的业务单据-多选基础资料表
- **表名：** t_fpm_acldeductionbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fpm_acldeductionbill |  | fentryid |
| 2 | pk_t_fpm_acldeductionbill |  | fpkid |

---

## 实占单据体-子表 t_fpm_acldeduction

- **表名称：** 实占单据体-子表
- **表名：** t_fpm_acldeduction

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | facldeductioncode | 实占（实际扣减）时机编码 | varchar | 1024 |  | √ | ' ' | 实占（实际扣减）时机编码 |
| 3 | faclbusinessbill | 业务单据 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 4 | facldeduction | 实占（实际扣减）时机 | varchar | 1024 |  | √ | ' ' | 实占（实际扣减）时机 |
| 5 | freleaseacltimecode | 更新/释放实占（实际扣减）时机编码 | varchar | 1024 |  | √ | ' ' | 更新/释放实占（实际扣减）时机编码 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | funacldeductioncode | 取消实占（实际扣减）时机编码 | varchar | 1024 |  | √ | ' ' | 取消实占（实际扣减）时机编码 |
| 8 | ffactbackamountfield | 实占返还（释放）的金额取值 | varchar | 50 |  | √ | ' ' | 实占返还（释放）的金额取值,枚举: |
| 9 | freleaseacltime | 实占返还（释放）时机 | varchar | 1024 |  | √ | ' ' | 实占返还（释放）时机 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | funacldeduction | 取消实占（实际扣减）时机 | varchar | 1024 |  | √ | ' ' | 取消实占（实际扣减）时机 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_acldeduction |  | fentryid |
| 2 | idx_fpm_acldeduction |  | fid |

---

## 控制执行时机配置（废弃）-多语言表 t_fpm_executetime_l

- **表名称：** 控制执行时机配置（废弃）-多语言表
- **表名：** t_fpm_executetime_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fpm_executetime_l |  | fid |
| 2 | pk_t_fpm_executetime_l |  | fpkid |
