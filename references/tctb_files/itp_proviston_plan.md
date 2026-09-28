# 计提方案-itp_proviston_plan

## 计提方案-主表 t_itp_proviston_plan

- **表名称：** 计提方案-主表
- **表名：** t_itp_proviston_plan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmethod | 计提方法 | varchar | 50 |  | √ | ' ' | 计提方法,枚举: advance :预缴方法 remittance :汇算方法 |
| 6 | fbooktype | 账簿类型 | varchar | 50 |  | √ | ' ' | 账簿类型,枚举: bdzt :本地账簿 jtzt :集团账簿 |
| 7 | fisdimprovision | 分维度计提 | bpchar | 1 |  | √ | '0' | 分维度计提 |
| 8 | ftaxsystem | 税收制度 | int8 | 64 |  | √ | 0 | 税收制度 bd_taxationsys |
| 9 | ftaxarea | 税收辖区 | int8 | 64 |  | √ | 0 | 税收辖区 bastax_taxareagroup |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fenddate | 有效期止 | timestamp | 0 |  |  | null | 有效期止 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fstartdate | 有效期起 | timestamp | 0 |  |  | null | 有效期起 |
| 16 | fprovisiondimension | 计提维度 | varchar | 50 |  | √ | ' ' | 计提维度,枚举: accountorg :核算组织 businessdimension :业务维度 |
| 17 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fcycle | 计提周期 | varchar | 50 |  | √ | ' ' | 计提周期,枚举: month :月 season :季 year :年 |
| 19 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 20 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | 税种 bd_taxcategory |
| 21 | fsystemset | 系统预设 | varchar | 50 |  | √ | ' ' | 系统预设,枚举: 1 :是 0 :否 |

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
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 税务组织映射方案 tctb_orgmapentity |
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

## 计提方案-多语言表 t_itp_proviston_plan_l

- **表名称：** 计提方案-多语言表
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
