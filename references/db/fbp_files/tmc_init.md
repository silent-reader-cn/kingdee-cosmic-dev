# 资金初始化-tmc_init

## 资金初始化-多语言表 t_tmc_init_l

- **表名称：** 资金初始化-多语言表
- **表名：** t_tmc_init_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tmc_init_l |  | fid,fname,fcomment |
| 2 | t_tmc_init_l_pkey |  | fpkid |

---

## 资金初始化-主表 t_tmc_init

- **表名称：** 资金初始化-主表
- **表名：** t_tmc_init

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdescentity | 目标实体 | varchar | 100 |  | √ | ' ' | 目标实体 |
| 6 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 7 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 8 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fsrcbillcount | 目标记录数 | int8 | 64 |  | √ | 0 | 目标记录数 |
| 10 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' |  |
| 11 | fsrcentity | 原实体 | varchar | 100 |  | √ | ' ' | 原实体 |
| 12 | fclasspath | 接口实现类 | varchar | 250 |  | √ | ' ' | 接口实现类 |
| 13 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 14 | fstatus | 数据状态 | bpchar | 5 |  | √ | '0' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fupdateresult | 升级结果 | text | 0 |  |  | null | 升级结果 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fsuccesstime | 升级完成时间 | timestamp | 0 |  |  | null | 升级完成时间 |
| 19 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 22 | fcontent | 升级内容 | varchar | 100 |  | √ | ' ' | 升级内容 |
| 23 | fsuccesscount | 完成记录数 | int8 | 64 |  | √ | 0 | 完成记录数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tmc_init_pkey |  | fid |
| 2 | idx_tmc_init |  | fnumber |
