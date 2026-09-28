# 计提规则-tctb_jtgz_rules

## 取数规则-子表 t_tctb_jtgz_rules_entry

- **表名称：** 取数规则-子表
- **表名：** t_tctb_jtgz_rules_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffconditionjson | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |
| 3 | fcompositejson_tag | 数据源_详情 | text | 0 |  |  | null | 数据源_详情 |
| 4 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | 数据源字段配置 tctb_datasource_entry |
| 5 | fadvancedconfjson | 取数逻辑 | varchar | 2000 |  | √ | ' ' | 取数逻辑 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 8 | fcompositejson | 数据源 | varchar | 255 |  | √ | ' ' | 数据源 |
| 9 | fcomposite | 高级运算 | bpchar | 1 |  | √ | '0' | 高级运算 |
| 10 | ftable | 数据源 | int8 | 64 |  | √ | 0 | 数据源配置 tctb_custom_datasource |
| 11 | fvatrate | 税率 | numeric | 23 | 2 | √ | 0 | 税率 |
| 12 | fbasedatatype | 数据源 | varchar | 50 |  | √ | ' ' | 数据源,枚举: tctb_datasource_entry :数据源字段配置 tpo_col_member :列维成员管理 |
| 13 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 14 | fadvancedconf | 取数逻辑 | varchar | 2000 |  | √ | ' ' | 取数逻辑 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | ffiltercondition | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |
| 17 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 18 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 cysldsqs :税额换算不含税价 jsflqs :含税价换算不含税价 bhsjhshsj :不含税价换算含税价 sehshsj :税额换算含税价 bhsjhsse :不含税价换算税额 zjjs :直接计数 gjqs :高级取数 yjjsflqs :预缴含税价换算不含税价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_jtgz_rules_entry |  | fentryid |
| 2 | idx_tctb_jtgz_rules_entry_fk |  | fid |

---

## 计提规则-主表 t_tctb_jtgz_rules

- **表名称：** 计提规则-主表
- **表名：** t_tctb_jtgz_rules

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 3 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fruletype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型,枚举: private :自用规则 public :可分配规则 |
| 8 | fprovistonitem | 计提事项 | int8 | 64 |  | √ | 0 | 计提事项 itp_proviston_item |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | ffilterjson | 规则启用条件 | varchar | 255 |  | √ | ' ' | 规则启用条件 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fissystem | 系统预设 | varchar | 50 |  | √ | ' ' | 系统预设,枚举: 0 :否 1 :是 |
| 15 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fdatasource | 数据源 | int8 | 64 |  | √ | 0 | 数据源配置 tctb_custom_datasource |
| 17 | fgeneratecondition | 生成计提单 | varchar | 50 |  | √ | ' ' | 生成计提单,枚举: ALL :全部 NTE-ZERO :计提税金≠0 |
| 18 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 19 | frulepurpose | 规则用途 | varchar | 50 |  | √ | ' ' | 规则用途,枚举: nssb :纳税申报 sjjt :税金计提 |
| 20 | ffilterjson_tag | 规则启用条件_详情 | text | 0 |  |  | null | 规则启用条件_详情 |
| 21 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | 税种 bd_taxcategory |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_jtgz_rules |  | fid |
| 2 | idx_t_tctb_jtgz_rules_1 |  | fnumber |

---

## 计提规则-多语言表 t_tctb_jtgz_rules_l

- **表名称：** 计提规则-多语言表
- **表名：** t_tctb_jtgz_rules_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_jtgz_rules_l_0 |  | fid,flocaleid |
| 2 | pk_tctb_jtgz_rules_l |  | fpkid |

---

## 报表类型-多选基础资料表 t_tctb_jtgz_rules_type

- **表名称：** 报表类型-多选基础资料表
- **表名：** t_tctb_jtgz_rules_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 36 |  | √ | ' ' | 模板类型 tpo_template_type |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_jtgz_rules_type |  | fpkid |
| 2 | idx_tctb_jtgz_rules_type_fk |  | fid |
