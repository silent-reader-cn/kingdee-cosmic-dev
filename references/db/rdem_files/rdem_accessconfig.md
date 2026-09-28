# 取数配置-rdem_accessconfig

## 取数配置-多语言表 t_rdem_accessconfig_l

- **表名称：** 取数配置-多语言表
- **表名：** t_rdem_accessconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rdem_accessconfig_l_0 |  | fid,flocaleid |
| 2 | pk_rdem_accessconfig_l |  | fpkid |

---

## 取数规则-子表 t_rdem_accessconf_entry

- **表名称：** 取数规则-子表
- **表名：** t_rdem_accessconf_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 rdem_datasource_entry](../rdem_files/rdem_datasource_entry.md) |
| 3 | fadvancedconfjson | 取数逻辑 | varchar | 2000 |  | √ | ' ' | 取数逻辑 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fconditionjson | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |
| 6 | fbizname | 业务名称 | varchar | 100 |  | √ | ' ' | 业务名称 |
| 7 | fvatrate | 增值税税率 | numeric | 23 | 2 | √ | 0 | 增值税税率 |
| 8 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 rdem_custom_datasource](../rdem_files/rdem_custom_datasource.md) |
| 9 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 10 | fadvancedconf | 取数逻辑 | varchar | 2000 |  | √ | ' ' | 取数逻辑 |
| 11 | ffiltercondition | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 14 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 sehsbhsj :税额换算不含税价 hsjhsbhsj :含税价换算不含税价 sehshsj :税额换算含税价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_accessconf_entry |  | fentryid |
| 2 | idx_rdem_accessconf_entry_fk |  | fid |

---

## 取数配置-主表 t_rdem_accessconfig

- **表名称：** 取数配置-主表
- **表名：** t_rdem_accessconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 4 | fyfgxbbxmid | 取数项目 | int8 | 64 |  | √ | 0 | [研发与高新报表项目 rdem_yfgxbbxm](../rdem_files/rdem_yfgxbbxm.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fruletype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型,枚举: private :自用规则 public :可分配规则 |
| 8 | fispreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fapplicablerule | 适用取数规则 | int8 | 64 |  | √ | 0 | [自定义数据源适用取数规则 tctb_datasource_peek_rule](../tctb_files/tctb_datasource_peek_rule.md) |
| 14 | freporttype | 报表类型 | varchar | 50 |  | √ | ' ' | 报表类型,枚举: gxyhmxb :高新优惠明细表 yfjjyhmxb :研发加计优惠明细表 |
| 15 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编号 | varchar | 100 |  | √ | ' ' | 编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rdem_accessconfig_m0 |  | fmasterid |
| 2 | pk_rdem_accessconfig |  | fid |
