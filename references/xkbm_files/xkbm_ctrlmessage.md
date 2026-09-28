# 预算控制提示语-xkbm_ctrlmessage

## 自定义预算内提示语-多语言表 t_xkbm_inctrlmsgentry_l

- **表名称：** 自定义预算内提示语-多语言表
- **表名：** t_xkbm_inctrlmsgentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmessage | 提示语 | varchar | 255 |  | √ | ' ' | 提示语 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_inctrlmsgentry_l |  | fpkid |
| 2 | idx_xkbm_inctrlmsgentry_l |  | fentryid,flocaleid |

---

## 自定义预算数为空提示语-多语言表 t_xkbm_noctrlmsgentry_l

- **表名称：** 自定义预算数为空提示语-多语言表
- **表名：** t_xkbm_noctrlmsgentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmessage | 提示语 | varchar | 255 |  | √ | ' ' | 提示语 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_noctrlmsgentry_l |  | fpkid |
| 2 | idx_xkbm_noctrlmsgentry_l |  | fentryid,flocaleid |

---

## 自定义预算外提示语-子表 t_xkbm_outctrlmsgentry

- **表名称：** 自定义预算外提示语-子表
- **表名：** t_xkbm_outctrlmsgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsuitcondition | 适用条件 | bpchar | 1 |  | √ | ' ' | 适用条件,枚举: 0 :所有 1 :所有（不适用预算数为空） 2 :预算数为空 3 :超预算 4 :未超预算 5 :按期累计 |
| 3 | fmessage | 提示语 | varchar | 255 |  | √ | ' ' | 提示语 |
| 4 | fpreset | 系统预置 | bpchar | 1 |  | √ | ' ' | 系统预置,枚举: 0 :否 1 :是 |
| 5 | fmessagestore | 提示语库 | int8 | 64 |  | √ | 0 | 预算控制提示语库 xkbm_ctrlmsgstore |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_outctrlmsgentry |  | fentryid |
| 2 | idx_xkbm_outctrlmsgentry_fid |  | fid |

---

## 预算控制提示语-多语言表 t_xkbm_ctrlmsg_l

- **表名称：** 预算控制提示语-多语言表
- **表名：** t_xkbm_ctrlmsg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fnobudgetmodel | 提示语范例 | varchar | 1000 |  | √ | ' ' | 提示语范例 |
| 4 | finbudgetmodel | 提示语范例 | varchar | 1000 |  | √ | ' ' | 提示语范例 |
| 5 | foutbudgetmodel | 提示语范例 | varchar | 1000 |  | √ | ' ' | 提示语范例 |
| 6 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 7 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 8 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_ctrlmsg_l |  | fid,flocaleid |
| 2 | pk_xkbm_ctrlmsg_l |  | fpkid |

---

## 自定义预算数为空提示语-子表 t_xkbm_noctrlmsgentry

- **表名称：** 自定义预算数为空提示语-子表
- **表名：** t_xkbm_noctrlmsgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsuitcondition | 适用条件 | bpchar | 1 |  | √ | ' ' | 适用条件,枚举: 0 :所有 1 :所有（不适用预算数为空） 2 :预算数为空 3 :超预算 4 :未超预算 5 :仅按期累计 |
| 3 | fmessage | 提示语 | varchar | 255 |  | √ | ' ' | 提示语 |
| 4 | fpreset | 系统预置 | bpchar | 1 |  | √ | ' ' | 系统预置,枚举: 0 :否 1 :是 |
| 5 | fmessagestore | 提示语库 | int8 | 64 |  | √ | 0 | 预算控制提示语库 xkbm_ctrlmsgstore |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_noctrlmsgentry_fid |  | fid |
| 2 | pk_xkbm_noctrlmsgentry |  | fentryid |

---

## 预算控制提示语-主表 t_xkbm_ctrlmsg

- **表名称：** 预算控制提示语-主表
- **表名：** t_xkbm_ctrlmsg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxkbmbusinessservice | 预算业务服务 | int8 | 64 |  | √ | 0 | 预算业务服务 xkbm_businessservice |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fnobudgetmodel | 提示语范例 | varchar | 1000 |  | √ | ' ' | 提示语范例 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fpresetdata | 是否系统预置 | bpchar | 1 |  | √ | ' ' | 是否系统预置 |
| 8 | fshowdimnumber | 显示维度编码 | bpchar | 1 |  | √ | ' ' | 显示维度编码 |
| 9 | finbudgetmodel | 提示语范例 | varchar | 1000 |  | √ | ' ' | 提示语范例 |
| 10 | feffectstatus | 生效状态 | bpchar | 1 |  | √ | ' ' | 生效状态,枚举: 0 :失效 1 :生效 |
| 11 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | foutbudgetmodel | 提示语范例 | varchar | 1000 |  | √ | ' ' | 提示语范例 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fsuitallrole | 适用于所有角色 | bpchar | 1 |  | √ | ' ' | 适用于所有角色 |
| 19 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 20 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 21 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_ctrlmsg |  | fid |
| 2 | idx_xkbm_ctrlmsg |  | fstatus,fxkbmbusinessservice,feffectstatus |

---

## 自定义预算内提示语-子表 t_xkbm_inctrlmsgentry

- **表名称：** 自定义预算内提示语-子表
- **表名：** t_xkbm_inctrlmsgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsuitcondition | 适用条件 | bpchar | 1 |  | √ | ' ' | 适用条件,枚举: 0 :所有 1 :所有（不适用预算数为空） 2 :预算数为空 3 :超预算 4 :未超预算 5 :按期累计 |
| 3 | fmessage | 提示语 | varchar | 255 |  | √ | ' ' | 提示语 |
| 4 | fpreset | 系统预置 | bpchar | 1 |  | √ | ' ' | 系统预置,枚举: 0 :否 1 :是 |
| 5 | fmessagestore | 提示语库 | int8 | 64 |  | √ | 0 | 预算控制提示语库 xkbm_ctrlmsgstore |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_inctrlmsgentry_fid |  | fid |
| 2 | pk_xkbm_inctrlmsgentry |  | fentryid |

---

## 自定义预算外提示语-多语言表 t_xkbm_outctrlmsgentry_l

- **表名称：** 自定义预算外提示语-多语言表
- **表名：** t_xkbm_outctrlmsgentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmessage | 提示语 | varchar | 255 |  | √ | ' ' | 提示语 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_outctrlmsgentry_l |  | fpkid |
| 2 | idx_xkbm_outctrlmsgentry_l |  | fentryid,flocaleid |

---

## 适用角色范围-子表 t_xkbm_ctrlmsgrole

- **表名称：** 适用角色范围-子表
- **表名：** t_xkbm_ctrlmsgrole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | froleid | 角色编码 | varchar | 36 |  | √ | ' ' | 通用角色 perm_role |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_ctrlmsgrole |  | fentryid |
| 2 | idx_xkbm_ctrlmsgrole_fid |  | fid |
