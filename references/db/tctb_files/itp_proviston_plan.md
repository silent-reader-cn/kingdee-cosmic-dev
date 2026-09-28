# 计税方案-itp_proviston_plan

## 计税方案-主表 t_itp_proviston_plan

- **表名称：** 计税方案-主表
- **表名：** t_itp_proviston_plan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmethod | 计提方法 | varchar | 50 |  | √ | ' ' | 计提方法,枚举: advance :预缴方法 remittance :汇算方法 |
| 6 | fbooktype | 账簿类型 | varchar | 50 |  | √ | ' ' | 账簿类型,枚举: bdzt :本地账簿 jtzt :集团账簿 |
| 7 | fisdimprovision | 分维度计税 | bpchar | 1 |  | √ | '0' | 分维度计税 |
| 8 | ftaxsystem | 税收制度 | int8 | 64 |  | √ | 0 | [税收制度 bd_taxationsys](../basedata_files/bd_taxationsys.md) |
| 9 | ftaxarea | 税收辖区 | int8 | 64 |  | √ | 0 | [税收辖区 bastax_taxareagroup](../basedata_files/bastax_taxareagroup.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fenddate | 有效期止 | timestamp | 0 |  |  | null | 有效期止 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fstartdate | 有效期起 | timestamp | 0 |  |  | null | 有效期起 |
| 16 | fprovisiondimension | 计税维度 | varchar | 50 |  | √ | ' ' | 计税维度,枚举: accountorg :核算组织 businessdimension :业务维度 |
| 17 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fcycle | 计税周期 | varchar | 50 |  | √ | ' ' | 计税周期,枚举: month :月 season :季 halfyear :半年 year :年 |
| 19 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 20 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 21 | fsystemset | 系统预设 | varchar | 50 |  | √ | ' ' | 系统预设,枚举: 1 :是 0 :否 |
| 22 | fplanuse | 方案用途 | varchar | 50 |  | √ | ' ' | 方案用途,枚举: 1 :税金计提 2 :纳税申报 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_itp_proviston_plan |  | fid |
| 2 | idx_proviston_plan_num |  | fnumber |

---

## 业务维度-多选基础资料表 t_tctb_business_dimension

- **表名称：** 业务维度-多选基础资料表
- **表名：** t_tctb_business_dimension

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [税务组织映射方案 tctb_orgmapentity](../tctb_files/tctb_orgmapentity.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_business_dimension |  | fpkid |
| 2 | idx_tctb_business_dimension_fk |  | fid |

---

## 计税方案-多语言表 t_itp_proviston_plan_l

- **表名称：** 计税方案-多语言表
- **表名：** t_itp_proviston_plan_l

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
| 1 | pk_itp_proviston_plan_l |  | fpkid |
| 2 | idx_itp_proviston_plan_l_0 |  | fid,flocaleid |

---

## 业务维度分录-子表 t_itp_proviston_plan_e

- **表名称：** 业务维度分录-子表
- **表名：** t_itp_proviston_plan_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffzproperty | 映射对象 | int8 | 64 |  | √ | 0 | [辅助属性定义 bd_auxproperty](../sbd_files/bd_auxproperty.md) |
| 3 | forgmap | 编码 | int8 | 64 |  | √ | 0 | [税务组织映射方案 tctb_orgmapentity](../tctb_files/tctb_orgmapentity.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_itp_proviston_plan_e_fk |  | fid |
| 2 | pk_itp_proviston_plan_e |  | fentryid |
