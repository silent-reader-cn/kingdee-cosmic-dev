# 调度执行程序-sch_taskdefine

## 参数分录-多语言表 t_sch_taskdefentry_l

- **表名称：** 参数分录-多语言表
- **表名：** t_sch_taskdefentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fparamdesc | 参数描述 | varchar | 512 |  | √ | ' ' | 参数描述 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fdesc | fdesc | varchar | 50 |  | √ | ' ' |  |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | varchar | 36 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sch_taskdefentry_l_pkey |  | fpkid |
| 2 | idx_sch_tdeef_l_001 |  | fentryid,flocaleid |

---

## 调度执行程序-多语言表 t_sch_taskdefine_l

- **表名称：** 调度执行程序-多语言表
- **表名：** t_sch_taskdefine_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 500 |  |  | null | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sch_taskdefine_l_pkey |  | fpkid |
| 2 | idx_sch_tdef_l_id |  | fid,flocaleid |

---

## 参数分录-子表 t_sch_taskdefentry

- **表名称：** 参数分录-子表
- **表名：** t_sch_taskdefentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fparamvalue | 默认值 | varchar | 512 |  |  | null | 默认值 |
| 3 | fparamname | 参数名称 | varchar | 36 |  | √ | ' ' | 参数名称 |
| 4 | fbasedatainfo | 基础资料详情 | text | 0 |  |  | null | 基础资料详情 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fparamtype | 参数类型 | varchar | 10 |  |  | null | 参数类型,枚举: 0 :文本 1 :整数 2 :长整数 3 :小数 4 :日期 5 :长日期 6 :时间 7 :布尔类型 8 :基础资料 9 :多选基础资料 |
| 7 | fparamdesc | 参数描述 | varchar | 512 |  |  | null | 参数描述 |
| 8 | fentryid | fentryid | varchar | 36 |  | √ | ' ' | id |
| 9 | fmust | 必录 | bpchar | 1 |  | √ | '1' | 必录 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sch_tdeef_001 |  | fid |
| 2 | t_sch_taskdefentry_pkey |  | fentryid |

---

## 调度执行程序-主表 t_sch_taskdefine

- **表名称：** 调度执行程序-主表
- **表名：** t_sch_taskdefine

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | frescheduled | 支持重新调度 | bpchar | 1 |  | √ | '0' | 支持重新调度 |
| 3 | fksscriptid | ks脚本id | varchar | 36 |  | √ | ' ' | ks脚本id |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | fclassname | 插件路径 | varchar | 200 |  |  | null | 插件路径 |
| 8 | fnumber | 编码 | varchar | 200 |  |  | null | 编码 |
| 9 | fappid | 所属应用 | varchar | 50 |  | √ | 'bos' | 所属应用,枚举: |
| 10 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 11 | fplugintype | 类型 | varchar | 10 |  | √ | '0' | 类型,枚举: 0 :Java 4 :脚本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sch_taskdefine_pkey |  | fid |
| 2 | idx_sch_tdef_001 |  | fclassname |
