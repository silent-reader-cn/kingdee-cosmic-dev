# 流程状态-plm_lc_status

## 流程状态-使用范围表 t_plmsm_lc_status_u

- **表名称：** 流程状态-使用范围表
- **表名：** t_plmsm_lc_status_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmsm_lc_status_u |  | fdataid,fuseorgid |
| 2 | idx_t_plmsm_lc_status_u_uo |  | fuseorgid |

---

## 单据体_正向校验-子表 t_plmsm_lc_status_val

- **表名称：** 单据体_正向校验-子表
- **表名：** t_plmsm_lc_status_val

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffailhandle | 校验不通过时 | varchar | 50 |  | √ | ' ' | 校验不通过时,枚举: 1 :取消并返回 2 :仅消息提醒 |
| 3 | findex | 执行顺序 | int8 | 64 |  | √ | 0 | 执行顺序 |
| 4 | fvalidatorname | 规则名称 | varchar | 50 |  | √ | ' ' | 规则名称 |
| 5 | fvalidatorld | 校验器 | int8 | 64 |  | √ | 0 | [生命周期校验器 plm_life_validator_lib](../plmsm_files/plm_life_validator_lib.md) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmsm_lc_status_val_fk |  | fid |
| 2 | pk_plmsm_lc_status_val |  | fentryid |

---

## 流程状态-多语言表 t_plmsm_lc_status_l

- **表名称：** 流程状态-多语言表
- **表名：** t_plmsm_lc_status_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmsm_lc_status_l |  | fpkid |
| 2 | idx_plmsm_lc_status_l_0 |  | fid,flocaleid |

---

## 单据体_操作-子表 t_plmsm_lc_status_act

- **表名称：** 单据体_操作-子表
- **表名：** t_plmsm_lc_status_act

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | factuatorparamter | 参数 | varchar | 255 |  | √ | ' ' | 参数 |
| 3 | factuatorparamter_tag | 参数_详情 | text | 0 |  |  | ' ' | 参数_详情 |
| 4 | findex | 执行顺序 | int8 | 64 |  | √ | 0 | 执行顺序 |
| 5 | factuatorname | 操作名称 | varchar | 50 |  | √ | ' ' | 操作名称 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | factuatorld | 执行器 | int8 | 64 |  | √ | 0 | [生命周期业务执行器 plm_life_actuator_lib](../plmsm_files/plm_life_actuator_lib.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmsm_lc_status_act |  | fentryid |
| 2 | idx_plmsm_lc_status_act_fk |  | fid |

---

## 流程状态-主表 t_plmsm_lc_status

- **表名称：** 流程状态-主表
- **表名：** t_plmsm_lc_status

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fcolor | fcolor | varchar | 7 |  | √ | ' ' |  |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fpiclcstatus | fpiclcstatus | varchar | 255 |  | √ | ' ' |  |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fpreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 14 | fpicturefield | 状态图片 | varchar | 255 |  | √ | ' ' | 状态图片 |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 20 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 1 :逐级分配 5 :全局共享 6 :管控范围内共享 7 :私有 |
| 21 | fpresetpic | 状态图标 | varchar | 255 |  | √ | ' ' | 状态图标 |
| 22 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 24 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 25 | falias | 别名 | varchar | 50 |  | √ | ' ' | 别名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plmsm_lc_status_createorg |  | fcreateorgid |
| 2 | idx_lc_status_createorg |  | fcreateorgid |
| 3 | pk_plmsm_lc_status |  | fid |
| 4 | idx_t_plmsm_lc_status_master |  | fmasterid |
