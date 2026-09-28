# 移动实体-mbase_mobentity

## 可见用户组-子表 t_mbase_mobentityusrgrp

- **表名称：** 可见用户组-子表
- **表名：** t_mbase_mobentityusrgrp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fusrgrp | 名称 | int8 | 64 |  | √ | 0 | [用户组 bos_usrgrp](../base_files/bos_usrgrp.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mbase_mobentityusrgrp_fid |  | fid |
| 2 | pk_t_mbase_mobentityusrgrp |  | fentryid |

---

## 移动实体-多语言表 t_mbase_mobentity_l

- **表名称：** 移动实体-多语言表
- **表名：** t_mbase_mobentity_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fvisibleusrgrptxt | 可见用户组文本 | varchar | 2000 |  |  | ' ' | 可见用户组文本 |
| 4 | fvisibleusertxt | 可见用户文本 | varchar | 2000 |  |  | ' ' | 可见用户文本 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fdescription | 描述 | varchar | 500 |  |  | ' ' | 描述 |
| 7 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mbase_mobentity_l |  | fpkid |
| 2 | idx_mbase_mobentity_l_idloc |  | fid,flocaleid |

---

## 可见用户-子表 t_mbase_mobentityuser

- **表名称：** 可见用户-子表
- **表名：** t_mbase_mobentityuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fuser | 姓名 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mbase_mobentityuser_fid |  | fid |
| 2 | pk_t_mbase_mobentityuser |  | fentryid |

---

## 移动实体-主表 t_mbase_mobentity

- **表名称：** 移动实体-主表
- **表名：** t_mbase_mobentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapproverid | fapproverid | int8 | 64 |  | √ | 0 |  |
| 3 | fapprovedate | fapprovedate | timestamp | 0 |  |  | null |  |
| 4 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | flogo | 图标 | varchar | 255 |  |  | ' ' | 图标 |
| 7 | fvisibleusrgrptxt | 可见用户组文本 | varchar | 2000 |  |  | ' ' | 可见用户组文本 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fdescription | 描述 | varchar | 500 |  |  | ' ' | 描述 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fbizappid | 应用id | varchar | 36 |  | √ | ' ' | [业务应用列表 bos_devp_bizapplist](../devnew_files/bos_devp_bizapplist.md) |
| 12 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: null : qing :轻应用 mobform :移动表单 mobbill :移动单据（布局）编辑 mobbilllist :移动单据（布局）列表 |
| 16 | fvisibleusertxt | 可见用户文本 | varchar | 2000 |  |  | ' ' | 可见用户文本 |
| 17 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fsystempreset | 系统预设 | varchar | 1 |  | √ | ' ' | 系统预设 |
| 19 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 20 | fformid | 表单标识 | varchar | 50 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mbase_mobentity |  | fid |
| 2 | idx_mbase_mobentity_fformid |  | fformid |
