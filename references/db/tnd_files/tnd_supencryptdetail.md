# 加解密任务-tnd_supencryptdetail

## 供应商用户-多选基础资料表 t_pds_supplierusers

- **表名称：** 供应商用户-多选基础资料表
- **表名：** t_pds_supplierusers

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 供应商用户 pur_supuser |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_supplierusers_bid |  | fbasedataid |
| 2 | pk_pds_supplierusers |  | fpkid |
| 3 | idx_pds_supplierusers_fid |  | fid |

---

## 加解密任务-主表 t_pds_supencryptdetail

- **表名称：** 加解密任务-主表
- **表名：** t_pds_supencryptdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 3 | fdecryptdate | 解密时间 | timestamp | 0 |  |  | null | 解密时间 |
| 4 | fterminatedate | 终止时间 | timestamp | 0 |  |  | null | 终止时间 |
| 5 | fissend | 是否发送 | bpchar | 1 |  | √ | '0' | 是否发送 |
| 6 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 7 | fbidderid | 当前处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fisdecrypt | 是否已解密 | bpchar | 1 |  | √ | '0' | 是否已解密 |
| 9 | fusername | CA用户名 | varchar | 50 |  | √ | ' ' | CA用户名 |
| 10 | fopentype | 开标类型 | bpchar | 1 |  | √ | ' ' | 开标类型,枚举: 1 :开资审标 2 :开标/开技术标 3 :开商务标 |
| 11 | fpackageid | 标段 | int8 | 64 |  | √ | 0 | 标段名称 pds_packagef7 |
| 12 | fencryptcode2 | 自动加密产生的解密验证码 | varchar | 100 |  | √ | ' ' | 自动加密产生的解密验证码 |
| 13 | fsenddate | 发送时间 | timestamp | 0 |  |  | null | 发送时间 |
| 14 | fisencrypt | 是否已加密 | bpchar | 1 |  | √ | '0' | 是否已加密 |
| 15 | fentityid | 来源单据标识 | varchar | 50 |  | √ | ' ' | 来源单据标识 |
| 16 | fencryptcode | 验证码 | varchar | 100 |  | √ | ' ' | 验证码 |
| 17 | fisterminate | 是否终止 | bpchar | 1 |  | √ | '0' | 是否终止 |
| 18 | fencryptdate | 加密时间 | timestamp | 0 |  |  | null | 加密时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_supencryptdetail |  | fid |
| 2 | idx_pds_supencryptdetail_bid |  | fbidderid |
| 3 | idx_pds_supencryptdetail_sid |  | fsupplierid |
| 4 | idx_pds_supencryptdetail_pid |  | fprojectid |
| 5 | idx_pds_supencryptdetail_pakid |  | fpackageid |
| 6 | idx_pds_supencryptdetail_oid |  | fopentype |
