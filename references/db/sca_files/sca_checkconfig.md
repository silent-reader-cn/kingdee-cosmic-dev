# 标准成本核算合法性检查配置-sca_checkconfig

## 标准成本核算合法性检查配置-多语言表 t_sca_checkconfig_l

- **表名称：** 标准成本核算合法性检查配置-多语言表
- **表名：** t_sca_checkconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 检查名称 | varchar | 255 |  | √ | ' ' | 检查名称 |
| 3 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_checkconfig_l_pkey |  | fpkid |
| 2 | index_sca_checkconfig_l |  | flocaleid,fname |

---

## 单据体-多语言表 t_sca_checkconfigentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_sca_checkconfigentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 2 | fdesc | 检查项描述 | varchar | 255 |  | √ | ' ' | 检查项描述 |
| 3 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_checkconfigentry_l_pkey |  | fpkid |
| 2 | index_sca_checkconfigentry_l |  | flocaleid,fdesc |

---

## 单据体-子表 t_sca_checkconfigentry

- **表名称：** 单据体-子表
- **表名：** t_sca_checkconfigentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fclass | 检查类 | varchar | 255 |  | √ | ' ' | 检查类 |
| 3 | fmethod | 检查方法 | varchar | 50 |  | √ | ' ' | 检查方法 |
| 4 | fsort | 排序 | int8 | 64 |  | √ | 0 | 排序 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | freusltentity | 检查详细页面实体 | varchar | 50 |  | √ | ' ' | 检查详细页面实体 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_sca_checkconfigentry |  | fclass,freusltentity |
| 2 | t_sca_checkconfigentry_pkey |  | fentryid |

---

## 标准成本核算合法性检查配置-主表 t_sca_checkconfig

- **表名称：** 标准成本核算合法性检查配置-主表
- **表名：** t_sca_checkconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | ftype | 检查类别 | varchar | 30 |  | √ | ' ' | 检查类别,枚举: 0 :卷算检查 1 :在产计算 2 :完工计算 3 :期末计算 4 :差异分摊检查 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | ftaskconfigid | 执行任务 | int8 | 64 |  | √ | 0 | [任务配置 sca_taskconfig](../aca_files/sca_taskconfig.md) |
| 6 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_checkconfig_pkey |  | fid |
| 2 | index_sca_checkconfig |  | ftype,ftaskconfigid |
