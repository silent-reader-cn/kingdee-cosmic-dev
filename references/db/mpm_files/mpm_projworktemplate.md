# 项目工作台模板-mpm_projworktemplate

## 部门范围-多选基础资料表 t_mpm_worktemplaterdept

- **表名称：** 部门范围-多选基础资料表
- **表名：** t_mpm_worktemplaterdept

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
| 1 | idx_mpm_worktemplaterdept |  | fid |
| 2 | pk_t_mpm_worktemplaterdept |  | fpkid |

---

## 部门范围-多选基础资料表 t_mpm_worktemplateddept

- **表名称：** 部门范围-多选基础资料表
- **表名：** t_mpm_worktemplateddept

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
| 1 | pk_t_mpm_worktemplateddept |  | fpkid |
| 2 | idx_mpm_worktemplateddept |  | fid |

---

## 项目工作台模板-主表 t_mpm_worktemplate

- **表名称：** 项目工作台模板-主表
- **表名：** t_mpm_worktemplate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | ftaskoptionalrange | 可选范围 | bpchar | 1 |  | √ | ' ' | 可选范围,枚举: A :全部 B :所属部门 C :所属部门及下级部门 D :自定义部门范围 E :本人参与的 |
| 6 | fissueoptionalrange | 可选范围 | bpchar | 1 |  | √ | ' ' | 可选范围,枚举: A :全部 B :所属部门 C :所属部门及下级部门 D :自定义部门范围 E :本人参与的 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | friskoptionalrange | 可选范围 | bpchar | 1 |  | √ | ' ' | 可选范围,枚举: A :全部 B :所属部门 C :所属部门及下级部门 D :自定义部门范围 E :本人参与的 |
| 9 | fdocoptionalrange | 可选范围 | bpchar | 1 |  | √ | ' ' | 可选范围,枚举: A :全部 B :所属部门 C :所属部门及下级部门 D :自定义部门范围 E :本人提交的 |
| 10 | fpuroptionalrange | 可选范围 | bpchar | 1 |  | √ | ' ' | 可选范围,枚举: A :全部 B :所属组织 C :所属部门 D :自定义组织范围 E :自定义部门范围 F :采购员为本人 |
| 11 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | fhouroptionalrange | 可选范围 | bpchar | 1 |  | √ | ' ' | 可选范围,枚举: A :全部 B :所属部门 C :所属部门及下级部门 D :自定义部门范围 E :本人参与的 |
| 13 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 20 | fschemelayoutid | 方案布局 | int8 | 64 |  | √ | 0 | [首页方案 portal_scheme](../portal_files/portal_scheme.md) |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_worktemplate |  | fid |
| 2 | idx_mpm_worktemplate |  | fnumber |

---

## 部门范围-多选基础资料表 t_mpm_worktemplatetdept

- **表名称：** 部门范围-多选基础资料表
- **表名：** t_mpm_worktemplatetdept

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
| 1 | pk_t_mpm_worktemplatetdept |  | fpkid |
| 2 | idx_mpm_worktemplatetdept |  | fid |

---

## 部门范围-多选基础资料表 t_mpm_worktemplatepdept

- **表名称：** 部门范围-多选基础资料表
- **表名：** t_mpm_worktemplatepdept

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
| 1 | idx_mpm_worktemplatepdept |  | fid |
| 2 | pk_t_mpm_worktemplatepdept |  | fpkid |

---

## 组织范围-多选基础资料表 t_mpm_worktemplateorg

- **表名称：** 组织范围-多选基础资料表
- **表名：** t_mpm_worktemplateorg

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
| 1 | pk_t_mpm_worktemplateorg |  | fpkid |
| 2 | idx_mpm_worktemplateorg |  | fid |

---

## 部门范围-多选基础资料表 t_mpm_worktemplatehdept

- **表名称：** 部门范围-多选基础资料表
- **表名：** t_mpm_worktemplatehdept

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
| 1 | idx_mpm_worktemplatehdept |  | fid |
| 2 | pk_t_mpm_worktemplatehdept |  | fpkid |

---

## 单据体-子表 t_mpm_worktempentry

- **表名称：** 单据体-子表
- **表名：** t_mpm_worktempentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisenable | 是否启用 | bpchar | 1 |  | √ | '0' | 是否启用 |
| 3 | fcardid | 卡片Id | int8 | 64 |  | √ | 0 | 卡片Id |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | ftabidentifier | 页签标识 | varchar | 50 |  | √ | ' ' | 页签标识 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ppe_worktementry_fid |  | fid |
| 2 | pk_mpm_worktempentry |  | fentryid |

---

## 项目工作台模板-多语言表 t_mpm_worktemplate_l

- **表名称：** 项目工作台模板-多语言表
- **表名：** t_mpm_worktemplate_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_worktemplate_l |  | fpkid |
| 2 | idx_mpm_worktemp_fidflid |  | fid,flocaleid |

---

## 部门范围-多选基础资料表 t_mpm_worktemplateridept

- **表名称：** 部门范围-多选基础资料表
- **表名：** t_mpm_worktemplateridept

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
| 1 | idx_mpm_worktemplateridept_fid |  | fid |
| 2 | pk_t_mpm_worktemplateridept |  | fpkid |
